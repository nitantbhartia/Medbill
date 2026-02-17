"""Tests for CMS transform helpers."""

import csv
from pathlib import Path

from cms_loader import (
    build_medicare_rates_csv_from_rvu,
    build_opps_rates_csv,
    build_ncci_ptp_csv,
)


def _write_csv(path: Path, rows: list[list[str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


class TestBuildMedicareRatesCsvFromRvu:
    def test_builds_expected_rows(self, tmp_path):
        in_csv = tmp_path / "pprrvu.csv"
        out_csv = tmp_path / "medicare.csv"
        rows = [
            ["meta", "", ""],
            ["HCPCS", "MOD", "DESCRIPTION", "CODE", "PAYMENT", "RVU", "PE RVU", "INDICATOR", "PE RVU", "INDICATOR", "RVU", "TOTAL", "TOTAL", "IND", "DAYS", "OP", "OP", "OP", "PROC", "SURG", "SURG", "SURG", "SURG", "IND", "BASE", "FACTOR", "PROCEDURES", "FLAG", "INDICATOR", "AMOUNT", "AMOUNT", "AMOUNT"],
            ["99285", "", "Emergency dept visit hi mdm", "A", "", "4.00", "0.65", "NA", "0.65", "", "0.48", "5.13", "5.13", "0", "XXX", "0", "0", "0", "0", "0", "0", "0", "0", "9", "", "33.4009", "09", "0", "99", "0.00", "0.00", "0.00"],
            ["A9999", "", "No pay code", "I", "", "0", "0", "", "0", "", "0", "0", "0", "0", "XXX", "0", "0", "0", "0", "0", "0", "0", "0", "9", "", "33.4009", "09", "0", "99", "0", "0", "0"],
            ["99285", "26", "Modifier duplicate", "A", "", "4.00", "0.65", "NA", "0.65", "", "0.48", "5.13", "5.13", "0", "XXX", "0", "0", "0", "0", "0", "0", "0", "0", "9", "", "33.4009", "09", "0", "99", "0.00", "0.00", "0.00"],
        ]
        _write_csv(in_csv, rows)

        count = build_medicare_rates_csv_from_rvu(str(in_csv), str(out_csv), 2026)
        assert count == 1

        with out_csv.open(newline="", encoding="utf-8") as f:
            out_rows = list(csv.DictReader(f))
        assert len(out_rows) == 1
        assert out_rows[0]["HCPCS"] == "99285"
        assert out_rows[0]["LOCALITY"] == "0000000"
        assert out_rows[0]["EFFECTIVE_YEAR"] == "2026"


class TestBuildOppsRatesCsv:
    def test_builds_and_dedupes_highest_payment(self, tmp_path):
        in_csv = tmp_path / "opps.csv"
        out_csv = tmp_path / "opps_out.csv"
        rows = [
            ["Title"],
            ["HCPCS Code", "Short Descriptor", "SI", "APC", "Relative Weight", "Payment Rate"],
            ["71046", "Chest xray", "S", "5522", "1.2", "72.00"],
            ["71046", "Chest xray", "S", "5522", "1.2", "65.00"],
            ["0000X", "No pay", "N", "", "", "0.00"],
        ]
        _write_csv(in_csv, rows)

        count = build_opps_rates_csv(str(in_csv), str(out_csv), 2026)
        assert count == 1

        with out_csv.open(newline="", encoding="utf-8") as f:
            out_rows = list(csv.DictReader(f))
        assert len(out_rows) == 1
        assert out_rows[0]["HCPCS"] == "71046"
        assert out_rows[0]["NATIONAL_PAYMENT_RATE"] == "72.00"


class TestBuildNcciPtpCsv:
    def test_parses_txt_and_formats_dates(self, tmp_path):
        txt = tmp_path / "ncci.txt"
        out_csv = tmp_path / "ncci_out.csv"
        txt.write_text(
            "\n".join(
                [
                    "Header\t\t\t\t\t\t",
                    "Column 1\tColumn 2\t*=in existence\tEffective\tDeletion\tModifier\tPTP Edit Rationale",
                    "\t\tprior to 1996\tDate\tDate\t0=not allowed\t",
                    "0001A\t0591T\t\t20220101\t20231231\t1\tRule",
                    "0001A\t36591\t\t20220101\t*\t0\tRule",
                    "bad\t\t\t20220101\t\t1\tRule",
                ]
            ),
            encoding="utf-8",
        )

        count = build_ncci_ptp_csv([str(txt)], str(out_csv))
        assert count == 2

        with out_csv.open(newline="", encoding="utf-8") as f:
            out_rows = list(csv.DictReader(f))
        assert len(out_rows) == 2
        assert out_rows[0]["EFFECTIVE_DATE"] == "2022-01-01"
        assert out_rows[0]["DELETION_DATE"] == "2023-12-31"
        assert out_rows[1]["DELETION_DATE"] == ""
