from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index_phash.csv"
OUT_FILE = INV / "phash_iguales.csv"

groups = defaultdict(list)

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["keep_drop_review"].strip().lower() != "keep":
            continue
        ph = row.get("phash", "").strip()
        if ph:
            groups[ph].append(row)

rows_out = []

for ph, items in groups.items():
    if len(items) > 1:
        items_sorted = sorted(
            items,
            key=lambda r: (
                r["final_label"],
                r["source_id"],
                r["original_filename"],
            )
        )
        for i, row in enumerate(items_sorted):
            rows_out.append({
                "phash": ph,
                "group_size": len(items_sorted),
                "group_rank": i + 1,
                "final_label": row["final_label"],
                "source_id": row["source_id"],
                "raw_split_or_folder": row["raw_split_or_folder"],
                "original_filename": row["original_filename"],
                "raw_path": row["raw_path"],
            })

with open(OUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "phash",
            "group_size",
            "group_rank",
            "final_label",
            "source_id",
            "raw_split_or_folder",
            "original_filename",
            "raw_path",
        ],
    )
    writer.writeheader()
    writer.writerows(rows_out)

print(f"CSV creado: {OUT_FILE}")
print(f"Filas exportadas: {len(rows_out)}")