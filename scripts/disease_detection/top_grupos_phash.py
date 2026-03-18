from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "phash_iguales.csv"
OUT_FILE = INV / "phash_iguales_top.csv"

rows = []

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["group_size_int"] = int(row["group_size"])
        rows.append(row)

rows.sort(
    key=lambda r: (
        -r["group_size_int"],
        r["phash"],
        r["group_rank"],
    )
)

top_n = 300
rows_out = rows[:top_n]

for row in rows_out:
    del row["group_size_int"]

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