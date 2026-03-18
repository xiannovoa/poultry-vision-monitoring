from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index.csv"
OUT_FILE = INV / "master_index_with_paths.csv"

rows = []

for row in csv.DictReader(open(IN_FILE, "r", encoding="utf-8-sig", newline="")):
    source_id = row["source_id"]
    folder = row["raw_split_or_folder"]
    filename = row["original_filename"]

    raw_path = ROOT / "01_raw" / source_id / folder / filename
    row["raw_path"] = str(raw_path)
    rows.append(row)

fieldnames = [
    "source_id",
    "raw_split_or_folder",
    "original_filename",
    "original_label",
    "final_label",
    "keep_drop_review",
    "notes",
    "raw_path",
]

with open(OUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"CSV creado: {OUT_FILE}")
print(f"Total filas: {len(rows)}")