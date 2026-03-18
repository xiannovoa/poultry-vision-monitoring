from pathlib import Path
import csv
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index_checked.csv"

counter = Counter()

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        counter[row["final_label"].strip()] += 1

print("Recuento por clase:")
for label, n in sorted(counter.items()):
    print(f"{label}: {n}")

print(f"Total: {sum(counter.values())}")