from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index_hashed.csv"
OUT_FILE = INV / "duplicados_exactos.csv"

groups = defaultdict(list)

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sha = row["sha256"].strip()
        groups[sha].append(row)

rows_out = []

for sha, items in groups.items():
    if len(items) > 1:
        items_sorted = sorted(
            items,
            key=lambda r: (
                r["source_id"],
                r["raw_split_or_folder"],
                r["original_filename"],
            )
        )
        for i, row in enumerate(items_sorted):
            row_out = {
                "sha256": sha,
                "group_size": len(items_sorted),
                "duplicate_rank": i + 1,
                "suggested_keep": "yes" if i == 0 else "no",
                "source_id": row["source_id"],
                "raw_split_or_folder": row["raw_split_or_folder"],
                "original_filename": row["original_filename"],
                "original_label": row["original_label"],
                "final_label": row["final_label"],
                "raw_path": row["raw_path"],
            }
            rows_out.append(row_out)

with open(OUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "sha256",
            "group_size",
            "duplicate_rank",
            "suggested_keep",
            "source_id",
            "raw_split_or_folder",
            "original_filename",
            "original_label",
            "final_label",
            "raw_path",
        ],
    )
    writer.writeheader()
    writer.writerows(rows_out)

print(f"CSV creado: {OUT_FILE}")
print(f"Filas exportadas: {len(rows_out)}")