from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index_checked.csv"

total = 0
empty_labels = 0

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += 1
        final_label = row["final_label"].strip()
        if final_label == "":
            empty_labels += 1

print(f"Total filas: {total}")
print(f"Final labels vacios: {empty_labels}")