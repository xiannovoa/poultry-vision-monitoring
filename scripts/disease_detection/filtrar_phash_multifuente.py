from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "phash_iguales.csv"
OUT_FILE = INV / "phash_multifuente.csv"

groups = defaultdict(list)

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        groups[row["phash"]].append(row)

rows_out = []

for phash, items in groups.items():
    fuentes = sorted(set(x["source_id"] for x in items))
    if len(fuentes) >= 2:
        items_sorted = sorted(
            items,
            key=lambda r: (
                r["final_label"],
                r["source_id"],
                r["original_filename"],
            )
        )
        for row in items_sorted:
            rows_out.append({
                "phash": row["phash"],
                "group_size": row["group_size"],
                "final_label": row["final_label"],
                "source_id": row["source_id"],
                "raw_split_or_folder": row["raw_split_or_folder"],
                "original_filename": row["original_filename"],
                "raw_path": row["raw_path"],
                "num_sources_in_group": len(fuentes),
                "sources_in_group": " | ".join(fuentes),
            })

with open(OUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "phash",
            "group_size",
            "final_label",
            "source_id",
            "raw_split_or_folder",
            "original_filename",
            "raw_path",
            "num_sources_in_group",
            "sources_in_group",
        ],
    )
    writer.writeheader()
    writer.writerows(rows_out)

print(f"CSV creado: {OUT_FILE}")
print(f"Filas exportadas: {len(rows_out)}")