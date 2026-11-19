"""Pre-deploy accuracy gate. Exits non-zero when scan accuracy drops. Run with --accept to save new baselines on purpose."""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import accuracy_gate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--accept", action="store_true", help="save the current scores as the new baseline")
    failures = accuracy_gate.run_gate(accept=parser.parse_args().accept)
    if failures:
        sys.exit("ACCURACY GATE FAILED\n" + "\n".join(failures))
    print("Accuracy gate passed.")


if __name__ == "__main__":
    main()
