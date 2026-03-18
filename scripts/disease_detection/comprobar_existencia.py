from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index_with_paths.csv"
OUT_FILE = INV / "master_index_checked.csv"

rows = []
missing = 0

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        raw_path = Path(row["raw_path"])
        exists = raw_path.exists()
        row["file_exists"] = "yes" if exists else "no"
        if not exists:
            missing += 1
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
    "file_exists",
]

with open(OUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"CSV creado: {OUT_FILE}")
print(f"Total filas: {len(rows)}")
print(f"Archivos no encontrados: {missing}")