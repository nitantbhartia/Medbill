#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PUBLIC_DIR="$ROOT_DIR/public"
mkdir -p "$PUBLIC_DIR"

curl -L --fail -o "$PUBLIC_DIR/aetna_eob_sample.pdf" \
  "https://assets.documentcloud.org/documents/1265368/aetna-explanation-of-benefits.pdf"

curl -L --fail -o "$PUBLIC_DIR/atlanticare_sample_bill.avif" \
  "https://www.atlanticare.org/sites/default/files/2024-11/a51f2ece21deff463f6eff170a1b1139.png"

if command -v sips >/dev/null 2>&1; then
  sips -s format png "$PUBLIC_DIR/atlanticare_sample_bill.avif" --out "$PUBLIC_DIR/atlanticare_sample_bill.png" >/dev/null
fi

echo "Fetched public samples into $PUBLIC_DIR"
