from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index_phash.csv"
OUT_FILE = INV / "casos_fuertes_multifuente.csv"

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

rows_out = []

for (final_label, original_filename), items in groups.items():
    fuentes = sorted(set(x["source_id"] for x in items))
    if len(fuentes) < 2:
        continue

    phashes = sorted(set(x.get("phash", "").strip() for x in items if x.get("phash", "").strip()))
    if len(phashes) != 1:
        continue

    items_sorted = sorted(
        items,
        key=lambda r: (
            r["source_id"],
            r["raw_split_or_folder"],
            r["original_filename"],
        )
    )

    for i, row in enumerate(items_sorted, start=1):
        rows_out.append({
            "final_label": final_label,
            "original_filename": original_filename,
            "phash": phashes[0],
            "group_size": len(items_sorted),
            "group_rank": i,
            "source_id": row["source_id"],
            "raw_split_or_folder": row["raw_split_or_folder"],
            "raw_path": row["raw_path"],
            "sources_in_group": " | ".join(fuentes),
        })

with open(OUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "final_label",
            "original_filename",
            "phash",
            "group_size",
            "group_rank",
            "source_id",
            "raw_split_or_folder",
            "raw_path",
            "sources_in_group",
        ],
    )
    writer.writeheader()
    writer.writerows(rows_out)

print(f"CSV creado: {OUT_FILE}")
print(f"Filas exportadas: {len(rows_out)}")