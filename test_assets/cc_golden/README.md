# ClaimCoach golden set

Denial letters with known answers, used to check that reading a letter stays accurate before a deploy.

## Format

Each case is an image (PNG or JPG) or a PDF plus one line in `expected.jsonl`:

```json
{"file": "aca_out_of_network.png", "claim_number": "KCH-7731904-02", "notice_date": "2026-03-09", "printed_deadline": "2026-09-05", "plan_type": "individual", "reason_key": "out_of_network"}
```

`printed_deadline` is the date a reader should arrive at: the printed date, or the notice date plus the printed window. Use `null` when the letter prints no deadline (for example a prior-authorization denial).

## Synthetic letters

The 5 letters here are drawn by `generate.py` and every name and number is invented. To regenerate the PNGs and `expected.jsonl` (same output every time):

    .venv312/bin/python test_assets/cc_golden/generate.py

## Adding real letters

Put redacted real letters, only with the owner's consent, in `test_assets/cc_golden/real/` with their own `real/expected.jsonl`. This repo is public, so real letters must never be committed. `test_assets/cc_golden/real/` is already in `.gitignore`.

## What the gate checks

`cc_accuracy.cc_gate()` (run by `accuracy_gate.run_gate`) reads every letter with Gemini and fails when:

- claim number, notice date or printed deadline is right less than `CC_GOLDEN_MIN_ACCURACY` of the time (exact match; claim numbers ignore spaces and case), or
- the file-by date computed from the reading is later than the expected `printed_deadline`, for any case.

It is skipped when `GEMINI_API_KEY` is unset or there are fewer than `CC_GOLDEN_MIN_CASES` cases.
