"""City ER Price Expose, Part 1: San Diego. The lighter, calmer cut: off-white notes look, 1.0x speed, about 18 s.

Every number drawn comes from expose_san_diego_facts.json. Usage:
    python3 render_light.py stills
    python3 render_light.py video    # out/billkarma_expose_sandiego_light_v1.mp4 and a contact sheet
"""

import math
import os
import subprocess
import sys
import wave

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

from render import FACTS, FPS, H, LEFT, CONTENT_W, OUT, SAFE_RIGHT, SR, W, ease_back, ease_in_out, ease_out, font, layer, noise_burst, prog, text_w, tone, wrap_caption

END = 18.0
SCENES = {"hook": 0.0, "table": 3.5, "high": 7.2, "low": 10.8, "ask": 14.5}
PAPER, WHITE, INK, MUTED, RULE = (248, 249, 250), (255, 255, 255), (26, 26, 26), (107, 114, 128), (229, 231, 235)
YELLOW, CORAL, AMBER = (255, 224, 102), (240, 113, 103), (245, 158, 11)
FINE, LABEL, BODY, CAPTION, TITLE, HERO = 25, 30, 38, 46, 76, 132

CITY, MILES = FACTS["CITY"], FACTS["MILES"]
NAME_A, NAME_B = FACTS["HOSP_A_NAME"], FACTS["HOSP_B_NAME"]
PRICE_A, PRICE_B = FACTS["PRICE_A_DISPLAY"], FACTS["PRICE_B_ROUNDED_DISPLAY"]
MULT_A, MULT_B = f"{FACTS['MULT_A_ROUNDED']}×", f"{FACTS['MULT_B_ROUNDED']}×"
DISCLOSURE = "Public hospital pricing data · published list prices · Not legal advice"  # "AI voice" joins when a voice does
CARD_NOTE = "List prices. Insured patients usually pay less."
CAPTIONS = [
    (0.0, 1.6, f"If you live in {CITY},"),
    (1.6, 3.5, "look at what one ER visit costs here."),
    (3.5, 5.6, f"I checked the published price files for two hospitals about {MILES} miles apart."),
    (5.6, 7.2, "Exact same Level 5 ER visit."),
    (7.2, 9.1, f"Scripps Mercy lists it at {PRICE_B}."),
    (9.1, 10.8, f"{MULT_B} what Medicare pays."),
    (10.8, 12.8, f"About {MILES} miles away, Kaiser San Diego still lists {PRICE_A}."),
    (12.8, 14.5, f"Over {MULT_A} Medicare."),
    (14.5, 16.0, "Every hospital has to publish these prices."),
    (16.0, 17.6, "Drop your city below and I'll check your local ERs next."),
]


def make_background():
    """Off-white paper with faint ruled lines, like a notes page."""
    rng = np.random.default_rng(11)
    base = np.zeros((H, W, 3), np.float32) + np.array(PAPER, np.float32)
    base += rng.normal(0, 1.1, (H // 2, W // 2)).repeat(2, 0).repeat(2, 1)[..., None]
    base[300::64, :, :] -= 5
    return Image.fromarray(np.clip(base, 0, 255).astype(np.uint8), "RGB")


BACKGROUND = make_background()


def fade(img, alpha):
    if alpha < 1:
        img.putalpha(img.getchannel("A").point(lambda v: int(v * alpha)))
    return img


def highlight(d, x0, x1, y0, y1, amount, alpha=150):
    """A highlighter pass, wiped left to right."""
    if amount > 0:
        d.rounded_rectangle((x0, y0, x0 + (x1 - x0) * amount, y1), 10, fill=YELLOW + (alpha,))


def soft_card(img, box, radius=26):
    """White card with a soft shadow."""
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    x0, y0, x1, y1 = box
    ImageDraw.Draw(shadow).rounded_rectangle((x0, y0 + 10, x1, y1 + 14), radius, fill=(17, 24, 39, 34))
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(18)))
    ImageDraw.Draw(img).rounded_rectangle(box, radius, fill=WHITE + (255,), outline=RULE + (255,), width=2)


def draw_hook(t):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    a = ease_out(prog(t, 0.0, 0.6))
    y = 420 + (1 - a) * 24
    d.text((LEFT, y), f"{CITY} ER", font=font(TITLE, "Bold"), fill=INK + (int(255 * a),))
    d.text((LEFT, y + 90), "Prices", font=font(TITLE, "Bold"), fill=INK + (int(255 * a),))
    b = ease_out(prog(t, 0.9, 0.6))
    if b > 0:
        f = font(HERO, "ExtraBold")
        label = f"{MULT_B} Medicare"
        f = font(96, "ExtraBold")
        w = text_w(d, label, f)
        highlight(d, LEFT - 10, LEFT + w + 14, 742, 800, ease_in_out(prog(t, 1.5, 0.8)))
        d.text((LEFT, 700 + (1 - b) * 20), label, font=f, fill=INK + (int(255 * b),))
        d.text((LEFT, 838), "for one Level 5 ER visit, at list price", font=font(LABEL, "Medium"), fill=MUTED + (int(255 * b),))
    return fade(img, 1 - ease_out(prog(t, SCENES["table"] - 0.35, 0.35)))


def draw_table(t):
    """Two-row comparison, names only: the prices arrive on the cards."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    a = ease_out(prog(t, SCENES["table"] + 0.1, 0.7))
    top = 470 + (1 - a) * 24
    soft_card(img, (LEFT, top, SAFE_RIGHT, top + 400))
    d = ImageDraw.Draw(img)
    d.text((LEFT + 36, top + 34), "Level 5 ER visit", font=font(BODY, "Bold"), fill=INK)
    d.text((LEFT + 36, top + 88), "Published list price", font=font(FINE, "Medium"), fill=MUTED)
    for i, name in enumerate((NAME_B, NAME_A)):
        y = top + 150 + i * 118
        d.line((LEFT + 36, y, SAFE_RIGHT - 36, y), fill=RULE, width=2)
        row = ease_out(prog(t, SCENES["table"] + 0.6 + i * 0.35, 0.5))
        name_font = font(LABEL, "SemiBold")
        while text_w(d, name, name_font) > CONTENT_W - 240 and name_font.size > 22:
            name_font = font(name_font.size - 1, "SemiBold")
        d.text((LEFT + 36, y + 59), name, font=name_font, fill=INK + (int(255 * row),), anchor="lm")
        d.rounded_rectangle((SAFE_RIGHT - 36 - 130, y + 44, SAFE_RIGHT - 36, y + 74), 15, fill=RULE + (int(255 * row),))
    pill = prog(t, SCENES["table"] + 1.9, 0.45)
    if pill > 0:
        label = f"about {MILES} miles apart"
        f = font(LABEL, "SemiBold")
        w = text_w(d, label, f) + 56
        cx, cy = LEFT + CONTENT_W / 2, top + 480
        s = ease_back(pill)
        d.rounded_rectangle((cx - w / 2 * s, cy - 32, cx + w / 2 * s, cy + 32), 32, fill=RULE + (255,))
        if pill > 0.5:
            d.text((cx, cy), label, font=f, fill=(75, 85, 99, int(255 * prog(pill, 0.5, 0.5))), anchor="mm")
    img = fade(img, a)
    return fade(img, 1 - ease_out(prog(t, SCENES["high"] - 0.35, 0.35)))


CARD_H, CARD_GAP, CARDS_TOP = 372, 34, 400
BAR_MAX = CONTENT_W - 72


def draw_card(img, top, name, price, mult, share, color, appear, bar, back):
    if appear <= 0:
        return
    card = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    soft_card(card, (LEFT, top, SAFE_RIGHT, top + CARD_H))
    d = ImageDraw.Draw(card)
    name_font = font(LABEL, "SemiBold")
    while text_w(d, name, name_font) > CONTENT_W - 72 and name_font.size > 22:
        name_font = font(name_font.size - 1, "SemiBold")
    d.text((LEFT + 36, top + 34), name, font=name_font, fill=INK)
    d.text((LEFT + 36, top + 82), "Level 5 ER visit · list price", font=font(FINE, "Medium"), fill=MUTED)
    d.text((LEFT + 34, top + 222), price, font=font(100, "ExtraBold"), fill=INK, anchor="ls")
    by = top + 256
    d.rounded_rectangle((LEFT + 36, by, LEFT + 36 + BAR_MAX, by + 26), 13, fill=(238, 240, 243, 255))
    fill_w = BAR_MAX * share * ease_in_out(bar)
    if fill_w > 26:
        d.rounded_rectangle((LEFT + 36, by, LEFT + 36 + fill_w, by + 26), 13, fill=color + (255,))
    label_a = prog(bar, 0.6, 0.4)
    if label_a > 0:
        f = font(BODY, "Bold")
        highlight(d, LEFT + 30, LEFT + 42 + text_w(d, mult, f), top + 308, top + 350, ease_out(label_a), 170)
        d.text((LEFT + 36, top + 304), mult, font=f, fill=INK + (int(255 * label_a),))
        d.text((LEFT + 36 + text_w(d, mult + " ", f) + 6, top + 310), "Medicare", font=font(LABEL, "Medium"), fill=INK + (int(255 * label_a),))
    alpha = ease_out(appear) * (1 - 0.93 * back)
    img.alpha_composite(fade(card, alpha), (0, int((1 - ease_out(appear)) * 60)))


def draw_cards(t):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    back = ease_in_out(prog(t, SCENES["ask"], 0.6))
    head = ease_out(prog(t, SCENES["high"], 0.4)) * (1 - 0.8 * back)
    d = ImageDraw.Draw(img)
    d.text((LEFT, 292), "billkarma.app", font=font(BODY, "Bold"), fill=INK + (int(255 * head),))
    d.text((LEFT, 344), f"{CITY} · Level 5 ER visit", font=font(FINE, "Medium"), fill=MUTED + (int(255 * head),))
    draw_card(img, CARDS_TOP, NAME_B, PRICE_B, MULT_B, 1.0, CORAL, prog(t, SCENES["high"] + 0.2, 0.6), prog(t, SCENES["high"] + 0.8, 1.2), back)
    draw_card(img, CARDS_TOP + CARD_H + CARD_GAP, NAME_A, PRICE_A, MULT_A, FACTS["PRICE_A"] / FACTS["PRICE_B"], AMBER,
              prog(t, SCENES["low"] + 0.2, 0.6), prog(t, SCENES["low"] + 0.8, 1.2), back)
    note = ease_out(prog(t, SCENES["high"] + 0.8, 0.5)) * (1 - back)
    ImageDraw.Draw(img).text((LEFT, CARDS_TOP + 2 * CARD_H + CARD_GAP + 30), CARD_NOTE, font=font(FINE, "Medium"), fill=MUTED + (int(255 * note),))
    return img


def draw_ask(t):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = LEFT + CONTENT_W / 2
    a = ease_out(prog(t, SCENES["ask"] + 0.4, 0.6))
    d.text((cx, 700), f"Part 1: {CITY}", font=font(LABEL, "SemiBold"), fill=MUTED + (int(255 * a),), anchor="mm")
    b = ease_out(prog(t, SCENES["ask"] + 0.7, 0.6))
    f = font(88, "ExtraBold")
    w = text_w(d, "Drop your city", f)
    highlight(d, cx - w / 2 - 12, cx + w / 2 + 12, 846, 900, ease_in_out(prog(t, SCENES["ask"] + 1.2, 0.7)))
    d.text((cx, 840 + (1 - b) * 16), "Drop your city", font=f, fill=INK + (int(255 * b),), anchor="mm")
    draw = ease_in_out(prog(t, SCENES["ask"] + 1.5, 0.7))
    if draw > 0:
        y0, y1 = 950, 1130
        ye = y0 + (y1 - y0) * draw
        d.line((cx, y0, cx, ye), fill=INK, width=8)
        if draw > 0.8:
            k = prog(draw, 0.8, 0.2)
            for side in (-1, 1):
                d.line((cx, ye, cx + side * 34 * k, ye - 38 * k), fill=INK, width=8)
    return img


def draw_caption(img, t):
    current = next((c for c in CAPTIONS if c[0] <= t < c[1]), None)
    if not current:
        return
    start, _, text = current
    d = ImageDraw.Draw(img)
    f = font(CAPTION, "Bold")
    lines = wrap_caption(d, text, f, 2 * (SAFE_RIGHT - W / 2) - 8)
    line_h = 62
    top = 1410 - line_h * len(lines) / 2
    appear = ease_out(prog(t, start, 0.2))
    space = text_w(d, " ", f)
    for i, line in enumerate(lines):
        x = W / 2 - text_w(d, " ".join(line), f) / 2
        y = top + i * line_h
        for word in line:
            w = text_w(d, word, f)
            if any(ch.isdigit() for ch in word):
                d.rounded_rectangle((x - 6, y + 22, x + w + 6, y + 56), 8, fill=YELLOW + (int(190 * appear),))
            d.text((x, y), word, font=f, fill=INK + (int(255 * appear),))
            x += w + space


def frame(t):
    img = BACKGROUND.convert("RGBA")
    if t < SCENES["table"]:
        img.alpha_composite(draw_hook(t))
    elif t < SCENES["high"]:
        img.alpha_composite(draw_table(t))
    else:
        img.alpha_composite(draw_cards(t))
        if t >= SCENES["ask"]:
            img.alpha_composite(draw_ask(t))
    ImageDraw.Draw(img).text((W / 2, 215), DISCLOSURE, font=font(FINE, "Medium"), fill=(75, 85, 99, 255), anchor="mm")
    draw_caption(img, t)
    return img.convert("RGB")


def build_audio(path):
    """Soft interface sounds and a light bed. No sub-bass. With no voice there is nothing to duck under yet."""
    total = int(END * SR)
    mix = np.zeros(total)
    n = np.arange(total) / SR

    def put(sound, t, gain):
        start = int(t * SR)
        end = min(total, start + len(sound))
        mix[start:end] += sound[: end - start] * gain

    bed = np.zeros(total)
    for freq, rate, phase in ((220.0, 0.13, 0.0), (277.18, 0.17, 1.3), (329.63, 0.11, 2.1), (440.0, 0.07, 0.6)):
        bed += np.sin(2 * np.pi * freq * n) * (0.55 + 0.45 * np.sin(2 * np.pi * rate * n + phase))
    envelope = np.clip(n / 0.8, 0, 1) * np.clip((END - 0.15 - n) / 1.2, 0, 1)
    mix += bed / 4 * 0.09 * envelope  # about 9% volume

    def brush(dur, seed):
        return noise_burst(dur, 1.5, 3, seed) * np.sin(np.linspace(0, np.pi, int(dur * SR))) ** 2

    def tap(freq):
        return layer(tone(freq, 0.16, 28), 0.4 * tone(freq * 2, 0.1, 40))

    put(brush(0.8, 1), 1.5, 0.10)
    put(tap(520), SCENES["table"] + 0.1, 0.16)
    put(tap(660), SCENES["table"] + 1.9, 0.14)
    put(tap(440), SCENES["high"] + 0.2, 0.20)
    put(brush(0.5, 2), SCENES["high"] + 1.5, 0.08)
    put(tap(494), SCENES["low"] + 0.2, 0.20)
    put(brush(0.5, 3), SCENES["low"] + 1.5, 0.08)
    put(brush(0.7, 4), SCENES["ask"] + 1.2, 0.10)
    put(tap(587), SCENES["ask"] + 0.7, 0.15)
    mix = np.clip(mix, -0.9, 0.9)
    with wave.open(path, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(SR)
        f.writeframes((mix * 32767).astype(np.int16).tobytes())


def render_video():
    os.makedirs(OUT, exist_ok=True)
    silent, wav = os.path.join(OUT, "light_silent.mp4"), os.path.join(OUT, "light_mix.wav")
    final, partial = os.path.join(OUT, "billkarma_expose_sandiego_light_v1.mp4"), os.path.join(OUT, "light_partial.mp4")
    encoder = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
         "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p", silent], stdin=subprocess.PIPE)
    for i in range(int(END * FPS)):
        encoder.stdin.write(frame(i / FPS).tobytes())
    encoder.stdin.close()
    if encoder.wait() != 0:
        raise SystemExit("ffmpeg failed while encoding frames")
    build_audio(wav)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", silent, "-i", wav, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", partial], check=True)
    os.replace(partial, final)
    return final


def contact_sheet(video):
    times = [0.5, 2.6, 4.4, 6.4, 8.0, 10.2, 11.6, 13.8, 15.4, 17.6]
    sheet = Image.new("RGB", (5 * 432 + 6 * 16, 2 * 768 + 3 * 16 + 2 * 34), (60, 64, 72))
    d = ImageDraw.Draw(sheet)
    for i, t in enumerate(times):
        path = os.path.join(OUT, f"light_sheet_{i}.png")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", video, "-frames:v", "1", path], check=True)
        x, y = 16 + (i % 5) * 448, 16 + (i // 5) * (768 + 50)
        sheet.paste(Image.open(path).resize((432, 768), Image.LANCZOS), (x, y))
        d.text((x, y + 772), f"{t:.1f}s", font=font(22, "SemiBold"), fill=(255, 255, 255))
    path = os.path.join(OUT, "expose_sandiego_light_contact_sheet.png")
    sheet.save(path)
    return path


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    if sys.argv[1:] == ["stills"]:
        for t in (2.8, 6.6, 10.4, 14.0, 17.0):
            frame(t).save(os.path.join(OUT, f"light_still_{t:04.1f}.png"))
    elif sys.argv[1:] == ["video"]:
        print(contact_sheet(render_video()))
    else:
        raise SystemExit(__doc__)
