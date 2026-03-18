from pathlib import Path
import csv
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index_dedup_multisource.csv"

status_counter = Counter()
class_counter = Counter()

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        status = row["keep_drop_review"].strip().lower()
        status_counter[status] += 1

        if status == "keep":
            class_counter[row["final_label"].strip()] += 1

print("Estado actual:")
for k in ["keep", "drop", "review"]:
    print(f"{k}: {status_counter.get(k, 0)}")

print("Clases en keep:")
for label, n in sorted(class_counter.items()):
    print(f"{label}: {n}")

print(f"Total keep: {sum(class_counter.values())}")