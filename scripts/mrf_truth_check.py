"""Compare insurers' real allowed amounts (from users' statements) with each hospital's published price files.

  python scripts/mrf_truth_check.py"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mrf_truth
from db import init_db

if __name__ == "__main__":
    init_db()
    print(json.dumps(mrf_truth.check(), indent=2))
