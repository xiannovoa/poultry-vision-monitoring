from pathlib import Path
import csv
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index_dedup_exact.csv"

counter = Counter()
total_keep = 0

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["keep_drop_review"].strip().lower() == "keep":
            label = row["final_label"].strip()
            counter[label] += 1
            total_keep += 1

print("Recuento por clase (solo keep):")
for label, n in sorted(counter.items()):
    print(f"{label}: {n}")

print(f"Total keep: {total_keep}")