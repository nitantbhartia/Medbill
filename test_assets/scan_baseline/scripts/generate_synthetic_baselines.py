#!/usr/bin/env python3
"""Generate deterministic synthetic medical bill/EOB scan fixtures.

Outputs PNG files plus a ground-truth JSONL manifest used for regression checks.
"""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "synthetic"
GT_PATH = ROOT / "synthetic_ground_truth.jsonl"

WIDTH = 1242
HEIGHT = 2208

PROVIDERS = [
    "North Valley Medical Group",
    "Cedar Park Family Medicine",
    "Riverside Outpatient Clinic",
    "Sunrise Health Partners",
    "Metro Community Hospital",
]

CPT_POOL = [
    ("99214", "Office/outpatient established visit"),
    ("99396", "Preventive visit est, 40-64"),
    ("80053", "Comprehensive metabolic panel"),
    ("71046", "Chest x-ray, 2 views"),
    ("36415", "Collection of venous blood"),
    ("G2211", "Visit complexity add-on"),
]


def money(v: float) -> str:
    return f"${v:,.2f}"


def base_canvas() -> tuple[Image.Image, ImageDraw.ImageDraw, ImageFont.FreeTypeFont]:
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("Arial.ttf", 33)
    except Exception:
        font = ImageFont.load_default()
    return img, draw, font


def draw_header(draw: ImageDraw.ImageDraw, font: ImageFont.ImageFont, title: str, provider: str) -> int:
    y = 80
    draw.rectangle([0, 0, WIDTH, 150], fill=(10, 130, 190))
    draw.text((40, 45), title, fill="white", font=font)
    draw.text((40, y + 100), provider, fill=(20, 20, 20), font=font)
    return y + 180


def render_statement(seed: int) -> tuple[Image.Image, dict[str, Any]]:
    rnd = random.Random(seed)
    provider = rnd.choice(PROVIDERS)
    img, draw, font = base_canvas()
    y = draw_header(draw, font, "Billing Statement", provider)

    line_items = []
    total = 0.0
    for _ in range(rnd.randint(3, 5)):
        cpt, desc = rnd.choice(CPT_POOL)
        amt = round(rnd.uniform(35, 420), 2)
        line_items.append({"cpt_code": cpt, "description": desc, "charged_amount": amt})
        total += amt

    insurance_paid = round(total * rnd.uniform(0.55, 0.92), 2)
    patient = round(max(0.0, total - insurance_paid), 2)

    draw.text((40, y), f"Outstanding balance: {money(patient)}", fill=(30, 30, 30), font=font)
    y += 70
    draw.text((40, y), f"Billed to Insurance: {money(total)}", fill=(30, 30, 30), font=font)
    y += 50
    draw.text((40, y), f"Insurance covered: -{money(insurance_paid)}", fill=(0, 110, 70), font=font)
    y += 90

    draw.text((40, y), "Detailed Account Information", fill=(10, 100, 155), font=font)
    y += 70

    for li in line_items:
        draw.text((40, y), f"{li['description']} - {li['cpt_code']}", fill=(40, 40, 40), font=font)
        draw.text((920, y), money(li["charged_amount"]), fill=(40, 40, 40), font=font)
        y += 55

    gt = {
        "doc_type": "statement",
        "provider_name": provider,
        "total_charged": round(total, 2),
        "total_patient_owes": patient,
        "line_items": line_items,
    }
    return img, gt


def render_eob(seed: int) -> tuple[Image.Image, dict[str, Any]]:
    rnd = random.Random(seed)
    provider = rnd.choice(PROVIDERS)
    img, draw, font = base_canvas()
    y = draw_header(draw, font, "Explanation of Benefits", provider)

    line_items = []
    total = 0.0
    paid_total = 0.0
    adj_total = 0.0

    draw.text((40, y), "Benefits Summary from Insurance", fill=(10, 100, 155), font=font)
    y += 70

    for _ in range(rnd.randint(2, 4)):
        cpt, desc = rnd.choice(CPT_POOL)
        charge = round(rnd.uniform(80, 520), 2)
        paid = round(charge * rnd.uniform(0.4, 0.9), 2)
        adj = round(charge * rnd.uniform(0.0, 0.2), 2)
        patient = round(max(0.0, charge - paid - adj), 2)
        total += charge
        paid_total += paid
        adj_total += adj
        line_items.append(
            {
                "cpt_code": cpt,
                "description": desc,
                "charged_amount": charge,
                "insurance_paid": paid,
                "insurance_adjustment": adj,
                "patient_responsibility": patient,
            }
        )

    patient_total = round(max(0.0, total - paid_total - adj_total), 2)

    draw.text((40, y), f"Outstanding balance: {money(patient_total)}", fill=(30, 30, 30), font=font)
    y += 55
    draw.text((40, y), f"Billed to Insurance: {money(total)}", fill=(30, 30, 30), font=font)
    y += 50
    draw.text((40, y), f"Insurance covered: -{money(paid_total)}", fill=(0, 110, 70), font=font)
    y += 50
    draw.text((40, y), f"Contract adjustment: -{money(adj_total)}", fill=(0, 110, 70), font=font)
    y += 50
    draw.text((40, y), f"Remaining responsibility: {money(patient_total)}", fill=(30, 30, 30), font=font)
    y += 90

    draw.text((40, y), "Detailed Claim Lines", fill=(10, 100, 155), font=font)
    y += 70
    for li in line_items:
        draw.text((40, y), f"{li['description']} - {li['cpt_code']}", fill=(40, 40, 40), font=font)
        draw.text((880, y), money(li["charged_amount"]), fill=(40, 40, 40), font=font)
        y += 50

    gt = {
        "doc_type": "eob",
        "provider_name": provider,
        "total_charged": round(total, 2),
        "total_patient_owes": patient_total,
        "line_items": line_items,
    }
    return img, gt


def render_portal(seed: int) -> tuple[Image.Image, dict[str, Any]]:
    rnd = random.Random(seed)
    provider = rnd.choice(PROVIDERS)
    img, draw, font = base_canvas()
    y = draw_header(draw, font, "Patient Portal Bill View", provider)

    c1, d1 = rnd.choice(CPT_POOL)
    c2, d2 = rnd.choice(CPT_POOL)
    a1 = round(rnd.uniform(180, 460), 2)
    a2 = round(rnd.uniform(120, 420), 2)
    total = round(a1 + a2, 2)
    covered = round(total * rnd.uniform(0.65, 0.9), 2)
    patient = round(max(0.0, total - covered), 2)

    draw.text((40, y), f"Outstanding balance {money(patient)}", fill=(30, 30, 30), font=font)
    y += 65
    draw.text((40, y), f"Billed to insurance {money(total)}", fill=(30, 30, 30), font=font)
    y += 45
    draw.text((40, y), f"Insurance covered -{money(covered)}", fill=(0, 110, 70), font=font)
    y += 45
    draw.text((40, y), f"Remaining responsibility {money(patient)}", fill=(30, 30, 30), font=font)
    y += 90

    draw.text((40, y), "Detailed Account Information", fill=(10, 100, 155), font=font)
    y += 60
    draw.text((40, y), f"{d1} - {c1}", fill=(40, 40, 40), font=font)
    draw.text((920, y), money(a1), fill=(40, 40, 40), font=font)
    y += 55
    draw.text((40, y), f"{d2} - {c2}", fill=(40, 40, 40), font=font)
    draw.text((920, y), money(a2), fill=(40, 40, 40), font=font)

    gt = {
        "doc_type": "portal",
        "provider_name": provider,
        "total_charged": total,
        "total_patient_owes": patient,
        "line_items": [
            {"cpt_code": c1, "description": d1, "charged_amount": a1},
            {"cpt_code": c2, "description": d2, "charged_amount": a2},
        ],
    }
    return img, gt


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    builders = [render_statement, render_eob, render_portal]
    records: list[dict[str, Any]] = []

    for i in range(18):
        builder = builders[i % len(builders)]
        img, gt = builder(1000 + i)
        name = f"synthetic_{gt['doc_type']}_{i+1:02d}.png"
        out_path = OUT_DIR / name
        img.save(out_path, format="PNG")
        gt["file"] = str(Path("synthetic") / name)
        records.append(gt)

    with GT_PATH.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec) + "\n")

    print(f"Generated {len(records)} synthetic fixtures in {OUT_DIR}")
    print(f"Ground truth: {GT_PATH}")


if __name__ == "__main__":
    main()
