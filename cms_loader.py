"""CMS data sourcing, transformation, and load helpers."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable
from urllib.request import urlretrieve
import zipfile

from data_refresh import refresh_medicare_rates, refresh_opps_rates, refresh_ncci_edits


RAW_CMS_URLS_2026 = {
    "rvu26a.zip": "https://www.cms.gov/files/zip/rvu26a-updated-12-29-2025.zip",
    "opps_addendum_b_jan2026.zip": "https://www.cms.gov/files/zip/january-2026-opps-addendum-b.zip",
    "ncci_2026q1_pra_f1.zip": (
        "https://www.cms.gov/files/zip/"
        "medicare-ncci-2026q1-practitioner-ptp-edits-ccipra-v320r0-f1.zip"
    ),
    "ncci_2026q1_pra_f2.zip": (
        "https://www.cms.gov/files/zip/"
        "medicare-ncci-2026q1-practitioner-ptp-edits-ccipra-v320r0-f2.zip"
    ),
    "ncci_2026q1_pra_f3.zip": (
        "https://www.cms.gov/files/zip/"
        "medicare-ncci-2026q1-practitioner-ptp-edits-ccipra-v320r0-f3.zip"
    ),
    "ncci_2026q1_pra_f4.zip": (
        "https://www.cms.gov/files/zip/"
        "medicare-ncci-2026q1-practitioner-ptp-edits-ccipra-v320r0-f4.zip"
    ),
}


def _parse_float(value: str) -> float | None:
    if value is None:
        return None
    cleaned = str(value).strip().replace(",", "").replace("$", "")
    if cleaned == "":
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None


def _to_date_ymd(value: str) -> str | None:
    val = (value or "").strip()
    if not val or val == "*":
        return None
    if len(val) == 8 and val.isdigit():
        return f"{val[0:4]}-{val[4:6]}-{val[6:8]}"
    return None


def download_cms_2026(raw_dir: str = "data/cms/raw") -> dict[str, str]:
    """Download required CMS 2026 source ZIP files into raw_dir."""
    raw_path = Path(raw_dir)
    raw_path.mkdir(parents=True, exist_ok=True)
    downloaded = {}
    for filename, url in RAW_CMS_URLS_2026.items():
        dest = raw_path / filename
        if not dest.exists():
            urlretrieve(url, dest)
        downloaded[filename] = str(dest)
    return downloaded


def _extract_zip(zip_path: Path, output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    files = []
    with zipfile.ZipFile(zip_path) as zf:
        for member in zf.namelist():
            zf.extract(member, output_dir)
            files.append(output_dir / member)
    return files


def build_medicare_rates_csv_from_rvu(
    pprrvu_csv_path: str,
    output_csv_path: str,
    effective_year: int = 2026,
) -> int:
    """
    Build medicare_rates import CSV from PPRRVU CSV.
    Uses national locality ('0000000') based on total RVUs * conversion factor.
    """
    input_path = Path(pprrvu_csv_path)
    output_path = Path(output_csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows_written = 0
    seen = set()
    with input_path.open(newline="", encoding="utf-8-sig") as f_in, output_path.open(
        "w", newline="", encoding="utf-8"
    ) as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)
        writer.writerow(
            [
                "HCPCS",
                "DESCRIPTION",
                "LOCALITY",
                "STATE",
                "NON_FACILITY_RATE",
                "FACILITY_RATE",
                "EFFECTIVE_YEAR",
            ]
        )

        header_found = False
        for row in reader:
            if not header_found:
                if len(row) > 25 and row[0] == "HCPCS" and "FACTOR" in row:
                    header_found = True
                continue

            if len(row) < 26:
                continue
            hcpcs = row[0].strip()
            modifier = row[1].strip()
            description = row[2].strip()
            total_non_fac_rvu = _parse_float(row[11]) or 0.0
            total_fac_rvu = _parse_float(row[12]) or 0.0
            conversion_factor = _parse_float(row[25])

            if not hcpcs or modifier or conversion_factor is None:
                continue
            if hcpcs in seen:
                continue

            non_facility_rate = round(total_non_fac_rvu * conversion_factor, 2)
            facility_rate = round(total_fac_rvu * conversion_factor, 2)

            if non_facility_rate <= 0 and facility_rate <= 0:
                continue

            writer.writerow(
                [
                    hcpcs,
                    description,
                    "0000000",
                    "",
                    f"{non_facility_rate:.2f}",
                    f"{facility_rate:.2f}",
                    str(effective_year),
                ]
            )
            seen.add(hcpcs)
            rows_written += 1

    return rows_written


def build_opps_rates_csv(
    addendum_b_csv_path: str,
    output_csv_path: str,
    effective_year: int = 2026,
) -> int:
    """Build OPPS import CSV from Addendum B CSV."""
    input_path = Path(addendum_b_csv_path)
    output_path = Path(output_csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    best_by_code: dict[str, tuple[str | None, str, float]] = {}
    with input_path.open(newline="", encoding="utf-8-sig", errors="ignore") as f_in:
        reader = csv.reader(f_in)

        header_found = False
        for row in reader:
            if not header_found:
                if row and row[0].strip() == "HCPCS Code":
                    header_found = True
                continue

            if len(row) < 6:
                continue
            code = row[0].strip()
            desc = row[1].strip()
            apc = row[3].strip() or None
            payment = _parse_float(row[5])

            if not code or payment is None or payment <= 0:
                continue
            if code not in best_by_code or payment > best_by_code[code][2]:
                best_by_code[code] = (apc, desc, payment)

    with output_path.open("w", newline="", encoding="utf-8") as f_out:
        writer = csv.writer(f_out)
        writer.writerow(
            ["HCPCS", "APC", "DESCRIPTION", "NATIONAL_PAYMENT_RATE", "EFFECTIVE_YEAR"]
        )
        for code, (apc, desc, payment) in sorted(best_by_code.items()):
            writer.writerow([code, apc or "", desc, f"{payment:.2f}", str(effective_year)])

    return len(best_by_code)


def build_ncci_ptp_csv(txt_paths: Iterable[str], output_csv_path: str) -> int:
    """Build NCCI import CSV from one or more CMS PTP TXT files."""
    output_path = Path(output_csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows_written = 0
    with output_path.open("w", newline="", encoding="utf-8") as f_out:
        writer = csv.writer(f_out)
        writer.writerow(
            ["COLUMN_1", "COLUMN_2", "EFFECTIVE_DATE", "DELETION_DATE", "MODIFIER_INDICATOR"]
        )

        for txt_path in txt_paths:
            with Path(txt_path).open(encoding="utf-8", errors="ignore") as f_in:
                reader = csv.reader(f_in, delimiter="\t")
                started = False
                for row in reader:
                    if not started:
                        if len(row) >= 2 and row[0].strip() == "Column 1" and row[1].strip() == "Column 2":
                            started = True
                        continue

                    if len(row) < 6:
                        continue
                    col1 = row[0].strip()
                    col2 = row[1].strip()
                    eff = _to_date_ymd(row[3])
                    deletion = _to_date_ymd(row[4])
                    modifier = row[5].strip() or "0"

                    if not col1 or not col2 or eff is None:
                        continue

                    writer.writerow([col1, col2, eff, deletion or "", modifier])
                    rows_written += 1

    return rows_written


def transform_cms_2026(
    raw_dir: str = "data/cms/raw",
    processed_dir: str = "data/cms/processed",
) -> dict[str, int]:
    """Transform downloaded CMS files into the app's expected CSV schemas."""
    raw_path = Path(raw_dir)
    processed_path = Path(processed_dir)
    processed_path.mkdir(parents=True, exist_ok=True)

    # Extract ZIP sources to stable subdirs.
    extracted_rvu = _extract_zip(raw_path / "rvu26a.zip", raw_path / "rvu26a")
    _extract_zip(raw_path / "opps_addendum_b_jan2026.zip", raw_path / "opps_jan2026")
    _extract_zip(raw_path / "ncci_2026q1_pra_f1.zip", raw_path / "ncci_pra_f1")
    _extract_zip(raw_path / "ncci_2026q1_pra_f2.zip", raw_path / "ncci_pra_f2")
    _extract_zip(raw_path / "ncci_2026q1_pra_f3.zip", raw_path / "ncci_pra_f3")
    _extract_zip(raw_path / "ncci_2026q1_pra_f4.zip", raw_path / "ncci_pra_f4")

    pprrvu_candidates = [p for p in extracted_rvu if p.name.endswith("_Jan_nonQPP.csv")]
    if not pprrvu_candidates:
        raise FileNotFoundError("Could not find PPRRVU *_Jan_nonQPP.csv in RVU ZIP")
    pprrvu_path = str(pprrvu_candidates[0])

    opps_csv_path = raw_path / "opps_jan2026" / "508 Version 2026 January Web Addendum B" / (
        "2026 January Web Addendum B.12.29.25.csv"
    )
    if not opps_csv_path.exists():
        raise FileNotFoundError(f"Could not find expected OPPS Addendum B CSV at {opps_csv_path}")

    ncci_txt_paths = sorted(
        str(p) for p in raw_path.glob("ncci_pra_f*/ccipra-v320r0-f*.[Tt][Xx][Tt]")
    )
    if len(ncci_txt_paths) < 4:
        raise FileNotFoundError("Could not find all 4 NCCI practitioner PTP TXT files")

    medicare_out = processed_path / "medicare_pfs_2026.csv"
    opps_out = processed_path / "opps_rates_2026.csv"
    ncci_out = processed_path / "ncci_ptp_2026q1_practitioner.csv"

    counts = {
        "medicare_rates": build_medicare_rates_csv_from_rvu(pprrvu_path, str(medicare_out), 2026),
        "opps_rates": build_opps_rates_csv(str(opps_csv_path), str(opps_out), 2026),
        "ncci_edits": build_ncci_ptp_csv(ncci_txt_paths, str(ncci_out)),
    }
    return counts


def load_transformed_cms_2026(processed_dir: str = "data/cms/processed") -> dict[str, int]:
    """Load transformed CSVs into the application database."""
    processed_path = Path(processed_dir)
    medicare_csv = processed_path / "medicare_pfs_2026.csv"
    opps_csv = processed_path / "opps_rates_2026.csv"
    ncci_csv = processed_path / "ncci_ptp_2026q1_practitioner.csv"

    if not (medicare_csv.exists() and opps_csv.exists() and ncci_csv.exists()):
        raise FileNotFoundError("Expected transformed CSVs were not found in data/cms/processed")

    return {
        "medicare_rates": refresh_medicare_rates(str(medicare_csv)),
        "opps_rates": refresh_opps_rates(str(opps_csv)),
        "ncci_edits": refresh_ncci_edits(str(ncci_csv)),
    }
