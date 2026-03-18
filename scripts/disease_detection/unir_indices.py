from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

input_files = [
    INV / "src01_main_index.csv",
    INV / "src02_poultry_index.csv",
    INV / "src03_extra_index.csv",
]

out_file = INV / "master_index.csv"

rows = []

for file_path in input_files:
    with open(file_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

with open(out_file, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "source_id",
            "raw_split_or_folder",
            "original_filename",
            "original_label",
            "final_label",
            "keep_drop_review",
            "notes",
        ],
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"CSV creado: {out_file}")
print(f"Total filas: {len(rows)}")