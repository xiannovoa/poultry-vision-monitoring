from pathlib import Path
import csv
from collections import Counter, defaultdict
from itertools import combinations

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "casos_fuertes_multifuente.csv"

groups = defaultdict(list)

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        key = (
            row["final_label"].strip(),
            row["original_filename"].strip().lower(),
            row["phash"].strip(),
        )
        groups[key].append(row)

pair_counter = Counter()

for _, items in groups.items():
    fuentes = sorted(set(x["source_id"] for x in items))
    for a, b in combinations(fuentes, 2):
        pair_counter[(a, b)] += 1

print("Solapamiento entre fuentes:")
for (a, b), n in sorted(pair_counter.items(), key=lambda x: (-x[1], x[0])):
    print(f"{a} <-> {b}: {n}")