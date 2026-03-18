from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index_phash.csv"

groups = defaultdict(list)

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["keep_drop_review"].strip().lower() != "keep":
            continue

        key = (
            row["final_label"].strip(),
            row["original_filename"].strip().lower(),
        )
        groups[key].append(row)

total_groups_multifuente = 0
groups_same_phash = 0
groups_diff_phash = 0

for key, items in groups.items():
    fuentes = set(x["source_id"] for x in items)
    if len(fuentes) < 2:
        continue

    total_groups_multifuente += 1

    phashes = set(x.get("phash", "").strip() for x in items if x.get("phash", "").strip())
    if len(phashes) == 1:
        groups_same_phash += 1
    else:
        groups_diff_phash += 1

print(f"Grupos mismo nombre + misma clase en varias fuentes: {total_groups_multifuente}")
print(f"De esos, grupos con mismo pHash: {groups_same_phash}")
print(f"De esos, grupos con pHash distinto: {groups_diff_phash}")