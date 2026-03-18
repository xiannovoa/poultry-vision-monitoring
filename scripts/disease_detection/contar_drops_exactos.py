from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index_dedup_exact.csv"

drops = 0
keeps = 0
reviews = 0

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        status = row["keep_drop_review"].strip().lower()
        if status == "drop":
            drops += 1
        elif status == "keep":
            keeps += 1
        elif status == "review":
            reviews += 1

print(f"keep: {keeps}")
print(f"drop: {drops}")
print(f"review: {reviews}")