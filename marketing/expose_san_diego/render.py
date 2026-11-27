"""City ER Price Expose, Part 1: San Diego. Faceless 1080x1920 video drawn with Pillow and piped to ffmpeg.

Every number drawn comes from expose_san_diego_facts.json. Usage:
    python3 render.py stills   # five full-size stills in out/
    python3 render.py video    # out/billkarma_expose_san_diego_v2.mp4 and a contact sheet
    python3 render.py sound    # rebuild the sound over frames already encoded
Marketing only: nothing in the deployed app imports this folder.
"""

import json
import math
import os
import subprocess
import sys
import wave

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
FACTS = json.load(open(os.path.join(HERE, "expose_san_diego_facts.json")))

W, H, FPS, SPEED = 1080, 1920, 30, 1.1
END = 14.8  # seconds of finished video; scene times below are finished-video seconds
SAFE_RIGHT = int(W * 0.79)  # cards, numbers and badges stay left of this
SAFE_BOTTOM = H - 380
LEFT = 64
CONTENT_W = SAFE_RIGHT - LEFT
SCENES = {"hook": 0.0, "code": 2.8, "high": 6.2, "low": 9.0, "ask": 11.8}

SLATE, PANEL, PANEL_EDGE = (18, 24, 32), (28, 36, 47), (52, 64, 80)
INK, MUTED, FAINT = (240, 243, 247), (150, 162, 178), (74, 86, 102)
YELLOW, RED, AMBER = (255, 212, 59), (240, 82, 72), (245, 158, 11)  # amber, not green: 8.1x Medicare is not a bargain

INTER = "/usr/share/fonts/opentype/inter/Inter-{}.otf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono{}.ttf"
_fonts = {}


def font(size, weight="Bold", mono=False):
    key = (size, weight, mono)
    if key not in _fonts:
        path = MONO.format("-Bold" if weight == "Bold" else "") if mono else INTER.format(weight)
        _fonts[key] = ImageFont.truetype(path, size)
    return _fonts[key]


# One type scale for the whole piece.
FINE, LABEL, BODY, CAPTION, TITLE, HERO = 25, 30, 38, 46, 68, 150

CITY = FACTS["CITY"].upper()
MILES = FACTS["MILES"]
NAME_A, NAME_B = FACTS["HOSP_A_NAME"].upper(), FACTS["HOSP_B_NAME"].upper()
PRICE_A, PRICE_B = FACTS["PRICE_A_DISPLAY"], FACTS["PRICE_B_DISPLAY"]
MULT_A, MULT_B = f"{FACTS['MULT_A']}x", f"{FACTS['MULT_B']}x"
HOOK = f"{FACTS['HOOK_MULT']}x"
CODE = FACTS["medicare"]["cpt_code"]
DISCLOSURE = "Public hospital pricing data · published list prices · Not legal advice"  # no voice in this cut
CARD_NOTE = "List prices. Insured patients usually pay less."

# (start, end, text): captions follow the script timings; words with digits are drawn yellow.
CAPTIONS = [
    (0.0, 1.3, f"If you live in {FACTS['CITY']},"),
    (1.3, 2.8, "look at what one ER visit costs here."),
    (2.8, 4.9, f"I pulled the published price files for two hospitals about {MILES} miles apart."),
    (4.9, 6.2, "Same Level 5 ER code."),
    (6.2, 7.8, f"Scripps Mercy lists it at {PRICE_B}."),
    (7.8, 9.0, f"{FACTS['HOOK_MULT']} times Medicare."),
    (9.0, 10.5, f"About {MILES} miles away, Kaiser San Diego still lists {PRICE_A}."),
    (10.5, 11.8, f"Over {int(FACTS['MULT_A'])} times Medicare."),
    (11.8, 13.2, "Every hospital has to publish these prices."),
    (13.2, 14.8, "Drop your city below and I'll pull your local ERs next."),
]


def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def prog(t, start, dur):
    return clamp((t - start) / dur)


def ease_out(x):
    return 1 - (1 - x) ** 3


def ease_in_out(x):
    return 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2


def ease_back(x):
    c = 1.70158
    return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2


def make_background():
    """Dark slate with a faint ledger grid, paper grain and a soft vignette."""
    rng = np.random.default_rng(7)
    base = np.zeros((H, W, 3), np.float32) + np.array(SLATE, np.float32)
    grain = rng.normal(0, 3.2, (H // 2, W // 2)).repeat(2, 0).repeat(2, 1)
    base += grain[..., None]
    base[::48, :, :] += 7
    base[:, ::48, :] += 7
    base[::240, :, :] += 6
    yy, xx = np.mgrid[0:H, 0:W]
    vignette = 1 - 0.38 * (((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H / 2) / (H * 0.75)) ** 2)
    return Image.fromarray(np.clip(base * vignette[..., None], 0, 255).astype(np.uint8), "RGB")


BACKGROUND = make_background()


def text_w(draw, text, f):
    return draw.textlength(text, font=f)


def shadow_text(img, xy, text, f, fill, anchor="la", blur=6, alpha=170):
    """Text with a soft shadow, drawn onto an RGBA image."""
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).text((xy[0], xy[1] + 3), text, font=f, fill=(0, 0, 0, alpha), anchor=anchor)
    img.alpha_composite(layer.filter(ImageFilter.GaussianBlur(blur)))
    ImageDraw.Draw(img).text(xy, text, font=f, fill=fill, anchor=anchor)


def marker_line(draw, x0, x1, y, amount, color, width=14):
    """A hand-drawn marker stroke: slightly wavy, drawn left to right as amount goes 0 to 1."""
    end = x0 + (x1 - x0) * amount
    points = [(x, y + 4 * math.sin(x / 37.0) + 2 * math.sin(x / 11.0)) for x in range(int(x0), int(end) + 1, 4)]
    if len(points) > 1:
        draw.line(points, fill=color, width=width, joint="curve")
        r = width // 2
        for px, py in (points[0], points[-1]):
            draw.ellipse((px - r, py - r, px + r, py + r), fill=color)


SHEET_TOP, ROW_H = 700, 76
SHEET_ROWS = 6
FOCUS_ROW = 3
ROW_Y = SHEET_TOP + 92 + FOCUS_ROW * ROW_H  # top of the highlighted row


def draw_sheet(t):
    """The marked-up price sheet: redacted rows around the one row this video is about."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    bottom = SHEET_TOP + 92 + SHEET_ROWS * ROW_H + 24
    d.rounded_rectangle((LEFT, SHEET_TOP, SAFE_RIGHT, bottom), 18, fill=PANEL + (255,), outline=PANEL_EDGE + (255,), width=2)
    d.text((LEFT + 28, SHEET_TOP + 30), "STANDARD CHARGES", font=font(FINE, "SemiBold", mono=True), fill=MUTED)
    d.text((SAFE_RIGHT - 28, SHEET_TOP + 30), "GROSS CHARGE", font=font(FINE, "SemiBold", mono=True), fill=MUTED, anchor="ra")
    d.line((LEFT + 28, SHEET_TOP + 78, SAFE_RIGHT - 28, SHEET_TOP + 78), fill=PANEL_EDGE, width=2)
    sweep = ease_in_out(prog(t, SCENES["code"] + 0.9, 0.55))
    for row in range(SHEET_ROWS):
        y = SHEET_TOP + 92 + row * ROW_H
        if row == FOCUS_ROW:
            if sweep > 0:  # yellow highlighter, wiped left to right
                x1 = LEFT + 16 + (CONTENT_W - 32) * sweep
                d.rounded_rectangle((LEFT + 16, y + 8, x1, y + ROW_H - 8), 8, fill=YELLOW + (64,))
            d.text((LEFT + 28, y + ROW_H / 2), f"CPT {CODE} · LEVEL 5 ER VISIT", font=font(LABEL, "Bold", mono=True), fill=INK, anchor="lm")
            continue
        widths = (200 + 53 * ((row * 5) % 4), 96 + 22 * (row % 3))  # redacted: other rows are not part of this story
        d.rounded_rectangle((LEFT + 28, y + 26, LEFT + 28 + widths[0], y + 50), 6, fill=FAINT + (150,))
        d.rounded_rectangle((SAFE_RIGHT - 28 - widths[1], y + 26, SAFE_RIGHT - 28, y + 50), 6, fill=FAINT + (150,))
        d.line((LEFT + 28, y + ROW_H, SAFE_RIGHT - 28, y + ROW_H), fill=PANEL_EDGE + (120,), width=1)
    return img


def draw_hook(t):
    """Scene 1 and 2: title, the gap and the sheet. The title block fades as the camera pushes in."""
    img = draw_sheet(t)
    head = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(head)
    rise = ease_out(prog(t, 0.05, 0.5))
    y = 286 + (1 - rise) * 40
    d.text((LEFT, y), f"{CITY} ER", font=font(TITLE, "ExtraBold"), fill=INK + (int(255 * rise),))
    d.text((LEFT, y + 78), "PRICES", font=font(TITLE, "ExtraBold"), fill=INK + (int(255 * rise),))
    pop = ease_back(prog(t, 0.55, 0.45)) if t >= 0.55 else 0
    if pop > 0:
        big = font(int(HERO * (0.6 + 0.4 * pop)), "Black")
        d.text((LEFT - 6, 604), HOOK, font=big, fill=RED, anchor="ls")
        gx = LEFT + text_w(d, HOOK, font(HERO, "Black")) + 18
        d.text((gx, 546), "THE MEDICARE", font=font(BODY, "ExtraBold"), fill=INK, anchor="ls")
        d.text((gx, 594), "RATE", font=font(BODY, "ExtraBold"), fill=INK, anchor="ls")
        gap_right = gx + text_w(d, "THE MEDICARE", font(BODY, "ExtraBold"))
        marker_line(d, LEFT, gap_right, 634, ease_out(prog(t, 1.05, 0.5)), RED + (235,))
    fade = 1 - ease_out(prog(t, SCENES["code"], 0.45))
    if fade < 1:
        head.putalpha(head.getchannel("A").point(lambda v: int(v * fade)))
    img.alpha_composite(head)
    return img


def draw_miles(img, t):
    """The distance pill pops under the sheet once the row is highlighted."""
    miles = prog(t, SCENES["code"] + 1.9, 0.4)
    if miles <= 0:
        return
    d = ImageDraw.Draw(img)
    label = f"{MILES} MILES APART"
    f = font(int(BODY * 1.35 * (0.7 + 0.3 * ease_back(miles))), "ExtraBold")
    cx, cy = LEFT + CONTENT_W / 2, 1160
    w = text_w(d, label, f) + 64
    d.rounded_rectangle((cx - w / 2, cy - 48, cx + w / 2, cy + 48), 48, fill=YELLOW + (255,))
    d.text((cx, cy), label, font=f, fill=SLATE, anchor="mm")


def zoomed(layer, t):
    """Camera move for scene 2: push in 1.0x to 1.25x on the highlighted row."""
    z = 1 + 0.25 * ease_in_out(prog(t, SCENES["code"], 0.9))
    if z == 1:
        return layer
    fx, fy = LEFT, ROW_Y + ROW_H / 2  # focus point: the start of the highlighted row
    tx, ty = LEFT, 760  # where the focus point lands on screen
    k = (z - 1) / 0.25
    ox, oy = fx + (tx - fx) * k, fy + (ty - fy) * k
    return layer.transform((W, H), Image.AFFINE, (1 / z, 0, fx - ox / z, 0, 1 / z, fy - oy / z), Image.BICUBIC)


CARD_H, CARD_GAP, CARDS_TOP = 380, 32, 396
BAR_MAX = CONTENT_W - 72


def draw_card(img, top, name, price, mult, share, color, appear, bar, dim):
    """One hospital card. share is this price divided by the higher price, so bars are to scale from zero."""
    if appear <= 0:
        return
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x0, x1 = LEFT, SAFE_RIGHT
    d.rounded_rectangle((x0, top, x1, top + CARD_H), 22, fill=PANEL + (255,), outline=PANEL_EDGE + (255,), width=2)
    d.rounded_rectangle((x0, top, x0 + 10, top + CARD_H), 5, fill=color + (255,))
    name_font = font(LABEL, "Bold")
    while text_w(d, name, name_font) > CONTENT_W - 72 and name_font.size > 22:
        name_font = font(name_font.size - 1, "Bold")
    d.text((x0 + 36, top + 34), name, font=name_font, fill=INK)
    d.text((x0 + 36, top + 84), f"CPT {CODE} · LIST PRICE", font=font(FINE, "SemiBold"), fill=MUTED)
    zoom = 1 + 0.25 * (1 - ease_out(prog(bar, 0.0, 0.6)))  # the number settles from 1.25x to 1.0x
    d.text((x0 + 34, top + 226), price, font=font(int(104 * zoom), "Black"), fill=INK, anchor="ls")
    by = top + 262
    d.rounded_rectangle((x0 + 36, by, x0 + 36 + BAR_MAX, by + 30), 15, fill=SLATE + (255,))
    fill_w = BAR_MAX * share * ease_out(bar)
    if fill_w > 30:
        d.rounded_rectangle((x0 + 36, by, x0 + 36 + fill_w, by + 30), 15, fill=color + (255,))
    if bar > 0.55:
        a = int(255 * prog(bar, 0.55, 0.3))
        d.text((x0 + 36, top + 312), mult, font=font(BODY, "ExtraBold"), fill=YELLOW + (a,))
        d.text((x0 + 36 + text_w(d, mult + " ", font(BODY, "ExtraBold")), top + 318), "the Medicare rate", font=font(LABEL, "Medium"), fill=INK + (a,))
    offset = (1 - ease_back(appear)) * 90
    alpha = ease_out(appear) * (0.16 if dim else 1.0)
    if alpha < 1:
        layer.putalpha(layer.getchannel("A").point(lambda v: int(v * alpha)))
    img.alpha_composite(layer, (0, int(offset)))


def draw_cards(t, dim=False):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    head = ease_out(prog(t, SCENES["high"], 0.3))
    d.text((LEFT, 282), "billkarma.app", font=font(BODY, "ExtraBold"), fill=INK + (int(255 * head * (0.4 if dim else 1)),))
    d.text((LEFT, 334), f"{CITY} · LEVEL 5 ER VISIT", font=font(FINE, "SemiBold"), fill=MUTED + (int(255 * head * (0.4 if dim else 1)),))
    share_a = FACTS["PRICE_A"] / FACTS["PRICE_B"]
    draw_card(img, CARDS_TOP, NAME_B, PRICE_B, MULT_B, 1.0, RED, prog(t, SCENES["high"] + 0.1, 0.35), prog(t, SCENES["high"] + 0.45, 0.9), dim)
    draw_card(img, CARDS_TOP + CARD_H + CARD_GAP, NAME_A, PRICE_A, MULT_A, share_a, AMBER,
              prog(t, SCENES["low"] + 0.1, 0.4), prog(t, SCENES["low"] + 0.5, 0.8), dim)
    note = ease_out(prog(t, SCENES["high"] + 0.5, 0.4)) * (0 if dim else 1)  # gone once the ask is up
    ImageDraw.Draw(img).text((LEFT, CARDS_TOP + 2 * CARD_H + CARD_GAP + 26), CARD_NOTE, font=font(FINE, "Medium"), fill=INK + (int(230 * note),))
    return img


def draw_ask(t):
    """Scene 5: the series tag, the ask, and an arrow drawn toward the comments."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = LEFT + CONTENT_W / 2  # centred in the area platform buttons leave free
    a = ease_out(prog(t, SCENES["ask"] + 0.15, 0.4))
    tag = f"PART 1: {CITY}"
    f = font(LABEL, "ExtraBold")
    w = text_w(d, tag, f) + 56
    d.rounded_rectangle((cx - w / 2, 700 - 34, cx + w / 2, 700 + 34), 34, outline=YELLOW + (int(255 * a),), width=3)
    d.text((cx, 700), tag, font=f, fill=YELLOW + (int(255 * a),), anchor="mm")
    b = ease_back(prog(t, SCENES["ask"] + 0.45, 0.45)) if t >= SCENES["ask"] + 0.45 else 0
    if b > 0:
        shadow_text(img, (cx, 850), "Drop your city", font(int(92 * (0.75 + 0.25 * b)), "Black"), INK, anchor="mm")
    draw = ease_in_out(prog(t, SCENES["ask"] + 0.95, 0.6))
    if draw > 0:  # arrow drawn by hand, top to bottom
        d = ImageDraw.Draw(img)
        y0, y1 = 940, 1170
        points = [(cx + 16 * math.sin((y - y0) / 62.0), y) for y in range(y0, int(y0 + (y1 - y0) * draw) + 1, 4)]
        if len(points) > 1:
            d.line(points, fill=YELLOW, width=12, joint="curve")
        if draw > 0.85:
            k = prog(draw, 0.85, 0.15)
            tipx, tipy = points[-1]
            for side in (-1, 1):
                d.line((tipx, tipy, tipx + side * 46 * k, tipy - 52 * k), fill=YELLOW, width=12)
            d.ellipse((tipx - 6, tipy - 6, tipx + 6, tipy + 6), fill=YELLOW)
    return img


def wrap_caption(draw, text, f, max_w):
    lines, line = [], []
    for word in text.split():
        if line and text_w(draw, " ".join(line + [word]), f) > max_w:
            lines.append(line)
            line = []
        line.append(word)
    return lines + [line]


def draw_caption(img, t):
    """Captions, centred on y=1410, kept inside the area platform buttons leave free."""
    current = next((c for c in CAPTIONS if c[0] <= t < c[1]), None)
    if not current:
        return
    start, _, text = current
    d = ImageDraw.Draw(img)
    f = font(CAPTION, "ExtraBold")
    max_w = 2 * (SAFE_RIGHT - W / 2) - 8
    lines = wrap_caption(d, text, f, max_w)
    line_h = 60
    top = 1410 - line_h * len(lines) / 2
    pad_x, pad_y = 26, 14
    widest = max(text_w(d, " ".join(line), f) for line in lines)
    appear = ease_out(prog(t, start, 0.14))
    plate = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(plate).rounded_rectangle((W / 2 - widest / 2 - pad_x, top - pad_y, W / 2 + widest / 2 + pad_x, top + line_h * len(lines) + pad_y - 6),
                                            18, fill=(8, 11, 15, int(205 * appear)))
    img.alpha_composite(plate)
    d = ImageDraw.Draw(img)
    space = text_w(d, " ", f)
    for i, line in enumerate(lines):
        x = W / 2 - text_w(d, " ".join(line), f) / 2
        y = top + i * line_h + (1 - appear) * 10
        for word in line:
            is_number = any(ch.isdigit() for ch in word)
            d.text((x, y), word, font=f, fill=(YELLOW if is_number else INK) + (int(255 * appear),))
            x += text_w(d, word, f) + space


def frame(t):
    """The finished frame at t seconds of the finished (1.1x) video."""
    img = BACKGROUND.convert("RGBA")
    if t < SCENES["high"]:
        layer = zoomed(draw_hook(t), t)
        draw_miles(layer, t)
        out = prog(t, SCENES["high"] - 0.18, 0.18)
        if out > 0:
            layer.putalpha(layer.getchannel("A").point(lambda v: int(v * (1 - out))))
        img.alpha_composite(layer)
    else:
        dim = t >= SCENES["ask"]
        if dim:
            k = prog(t, SCENES["ask"], 0.3)
            bright, dark = draw_cards(t, False), draw_cards(t, True)
            img.alpha_composite(Image.blend(bright, dark, ease_out(k)))
            img.alpha_composite(draw_ask(t))
        else:
            img.alpha_composite(draw_cards(t))
    shadow_text(img, (W / 2, 215), DISCLOSURE, font(FINE, "Medium"), (255, 255, 255, 255), anchor="mm", blur=5, alpha=200)
    draw_caption(img, t)
    return img.convert("RGB")


# ---------------------------------------------------------------- sound (numpy only)
SR = 44100


def tone(freq, dur, decay, sr=SR):
    n = np.arange(int(dur * sr)) / sr
    return np.sin(2 * np.pi * freq * n) * np.exp(-n * decay)


def noise_burst(dur, decay, lowpass, seed):
    rng = np.random.default_rng(seed)
    x = rng.normal(0, 1, int(dur * SR))
    kernel = np.ones(lowpass) / lowpass
    x = np.convolve(x, kernel, mode="same")
    n = np.arange(len(x)) / SR
    return x / (np.abs(x).max() + 1e-9) * np.exp(-n * decay)


def layer(*sounds):
    """Sum sounds of different lengths."""
    out = np.zeros(max(len(x) for x in sounds))
    for x in sounds:
        out[: len(x)] += x
    return out


def build_audio(path):
    """Effects and a quiet pulse bed, laid out on the pre-speed timeline and mixed in numpy."""
    total = int(END * SPEED * SR)
    mix = np.zeros(total)

    def put(sound, t_final, gain):
        start = int(t_final * SPEED * SR)
        end = min(total, start + len(sound))
        mix[start:end] += sound[: end - start] * gain

    n = np.arange(total) / SR
    beat = 0.5 + 0.5 * np.sin(2 * np.pi * 2.0 * n - np.pi / 2)  # two pulses a second
    bed = (np.sin(2 * np.pi * 55 * n) * 0.7 + np.sin(2 * np.pi * 110 * n) * 0.3) * beat ** 3
    bed += 0.25 * np.sin(2 * np.pi * 164.8 * n) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.11 * n))
    fade = np.clip(n / 0.4, 0, 1)
    mix += bed * 0.10 * fade  # about 10% volume

    put(layer(tone(180, 0.25, 14), 0.5 * noise_burst(0.12, 40, 6, 1)), 0.55, 0.55)  # the gap number lands
    put(noise_burst(0.5, 4, 3, 2) * np.linspace(0.3, 1, int(0.5 * SR)), 1.05, 0.30)  # marker stroke
    sweep = noise_burst(0.55, 2, 2, 3) * np.sin(np.linspace(0, np.pi, int(0.55 * SR)))
    put(sweep, SCENES["code"] + 0.9, 0.28)  # highlighter
    put(tone(660, 0.18, 22) + 0.6 * tone(990, 0.18, 26), SCENES["code"] + 1.9, 0.45)  # distance pops
    thud_n = np.arange(int(0.6 * SR)) / SR
    thud = np.sin(2 * np.pi * (95 * thud_n - 60 * thud_n ** 2)) * np.exp(-thud_n * 7)
    put(layer(thud, 0.4 * noise_burst(0.08, 60, 12, 4)), SCENES["high"] + 0.1, 0.95)  # heavy thud, higher price
    for i in range(9):  # bar-fill ticks, slowing as the bar settles
        put(tone(1500, 0.03, 120), SCENES["high"] + 0.45 + 0.9 * ease_out(i / 9) * 0.8, 0.22)
    put(layer(tone(1046.5, 0.9, 5), 0.6 * tone(1568, 0.9, 6), 0.3 * tone(2093, 0.7, 8)), SCENES["low"] + 0.1, 0.40)  # chime, lower price
    for i in range(7):
        put(tone(1700, 0.03, 120), SCENES["low"] + 0.5 + 0.8 * ease_out(i / 7) * 0.8, 0.20)
    put(noise_burst(0.35, 6, 40, 5), SCENES["ask"], 0.35)  # cards dim
    put(tone(523.25, 0.3, 12) + 0.5 * tone(784, 0.3, 14), SCENES["ask"] + 0.45, 0.40)  # the ask lands
    mix /= max(1.0, np.abs(mix).max() / 0.89)
    with wave.open(path, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(SR)
        f.writeframes((mix * 32767).astype(np.int16).tobytes())


def render_video(reuse_frames=False):
    os.makedirs(OUT, exist_ok=True)
    raw, wav = os.path.join(OUT, "silent_prespeed.mp4"), os.path.join(OUT, "mix.wav")
    final, partial = os.path.join(OUT, "billkarma_expose_san_diego_v2.mp4"), os.path.join(OUT, "partial.mp4")
    frames = 0 if reuse_frames else math.ceil(END * SPEED * FPS)
    if not reuse_frames:
        encoder = subprocess.Popen(
            ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
             "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", raw], stdin=subprocess.PIPE)
        for i in range(frames):
            encoder.stdin.write(frame(i / FPS / SPEED).tobytes())
        encoder.stdin.close()
        if encoder.wait() != 0:
            raise SystemExit("ffmpeg failed while encoding frames")
    build_audio(wav)
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-i", wav, "-filter_complex",
         f"[0:v]setpts=PTS/{SPEED},fps={FPS}[v];[1:a]atempo={SPEED}[a]", "-map", "[v]", "-map", "[a]",
         "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
         "-t", str(END), "-movflags", "+faststart", partial], check=True)
    os.replace(partial, final)
    return final


def contact_sheet(video):
    """Ten frames pulled from the finished file, two rows of five."""
    times = [0.4, 1.6, 3.4, 5.4, 6.6, 8.4, 9.5, 11.2, 12.4, 14.4]
    thumbs = []
    for i, t in enumerate(times):
        path = os.path.join(OUT, f"sheet_{i}.png")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", video, "-frames:v", "1", path], check=True)
        thumbs.append(Image.open(path).resize((432, 768), Image.LANCZOS))
    sheet = Image.new("RGB", (5 * 432 + 6 * 16, 2 * 768 + 3 * 16 + 2 * 34), (12, 14, 18))
    d = ImageDraw.Draw(sheet)
    for i, thumb in enumerate(thumbs):
        x, y = 16 + (i % 5) * 448, 16 + (i // 5) * (768 + 50)
        sheet.paste(thumb, (x, y))
        d.text((x, y + 772), f"{times[i]:.1f}s", font=font(22, "SemiBold"), fill=INK)
    path = os.path.join(OUT, "expose_san_diego_contact_sheet.png")
    sheet.save(path)
    return path


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    if sys.argv[1:] == ["stills"]:
        for t in (1.9, 5.6, 8.6, 11.3, 13.9):
            frame(t).save(os.path.join(OUT, f"still_{t:04.1f}.png"))
    elif sys.argv[1:] in (["video"], ["sound"]):  # "sound" rebuilds the mix over frames already encoded
        print(contact_sheet(render_video(reuse_frames=sys.argv[1] == "sound")))
    else:
        raise SystemExit(__doc__)
