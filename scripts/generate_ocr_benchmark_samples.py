"""Generate synthetic OCR benchmark fixtures (truth + noisy predictions + images)."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


def _write_bill_image(path: Path, provider: str, lines: list[dict], total: float, blur: bool = False) -> None:
    img = Image.new("RGB", (1200, 1600), "white")
    draw = ImageDraw.Draw(img)
    y = 60
    draw.text((60, y), f"Provider: {provider}", fill="black")
    y += 50
    draw.text((60, y), "Date: 2026-02-18", fill="black")
    y += 60
    draw.text((60, y), "CPT      Description                          Amount", fill="black")
    y += 40
    for row in lines:
        draw.text((60, y), f"{row['cpt_code']:<8} {row['description'][:30]:<30} ${row['charged_amount']:,.2f}", fill="black")
        y += 34
    y += 20
    draw.text((60, y), f"TOTAL CHARGED: ${total:,.2f}", fill="black")

    if blur:
        img = img.filter(ImageFilter.GaussianBlur(radius=1.8))
    img.save(path)


def main() -> None:
    root = Path("data/ocr_benchmark")
    root.mkdir(parents=True, exist_ok=True)

    samples = [
        {
            "id": "sample_clean_1",
            "provider_name": "Memorial Regional Hospital",
            "total_charged": 5700.0,
            "line_items": [
                {"cpt_code": "99285", "description": "ER Visit Level 5", "charged_amount": 4500.0},
                {"cpt_code": "71046", "description": "Chest X-Ray 2 views", "charged_amount": 1200.0},
            ],
        },
        {
            "id": "sample_blurry_1",
            "provider_name": "Aspirus Iron River Hospital",
            "total_charged": 1340.0,
            "line_items": [
                {"cpt_code": "80053", "description": "Comprehensive Metabolic Panel", "charged_amount": 340.0},
                {"cpt_code": "93000", "description": "EKG 12 lead", "charged_amount": 1000.0},
            ],
        },
        {
            "id": "sample_screenshot_1",
            "provider_name": "Broward Health Medical Center",
            "total_charged": 2625.0,
            "line_items": [
                {"cpt_code": "74177", "description": "CT Abdomen/Pelvis", "charged_amount": 2200.0},
                {"cpt_code": "85025", "description": "CBC", "charged_amount": 425.0},
            ],
        },
    ]

    manifest = {"samples": []}
    for s in samples:
        truth_path = root / f"{s['id']}.truth.json"
        pred_path = root / f"{s['id']}.pred.json"
        img_path = root / f"{s['id']}.png"

        truth = {
            "provider_name": s["provider_name"],
            "total_charged": s["total_charged"],
            "line_items": s["line_items"],
        }
        # Purposefully noisy predicted payload to benchmark future improvements.
        pred = {
            "provider_name": s["provider_name"] if "blurry" not in s["id"] else "Aspirus Iron Rivr Hospital",
            "total_charged": s["total_charged"] if "screenshot" not in s["id"] else s["total_charged"] + 5,
            "line_items": [
                {
                    "cpt_code": row["cpt_code"] if i == 0 else row["cpt_code"],
                    "description": row["description"],
                    "charged_amount": row["charged_amount"] if i == 0 else (row["charged_amount"] + (25 if "blurry" in s["id"] else 0)),
                }
                for i, row in enumerate(s["line_items"])
            ],
        }

        truth_path.write_text(json.dumps(truth, indent=2))
        pred_path.write_text(json.dumps(pred, indent=2))
        _write_bill_image(
            img_path,
            s["provider_name"],
            s["line_items"],
            s["total_charged"],
            blur=("blurry" in s["id"]),
        )
        manifest["samples"].append(
            {
                "id": s["id"],
                "image": img_path.name,
                "truth_json": truth_path.name,
                "prediction_json": pred_path.name,
            }
        )

    (root / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print({"generated_samples": len(samples), "manifest": str(root / "manifest.json")})


if __name__ == "__main__":
    main()
