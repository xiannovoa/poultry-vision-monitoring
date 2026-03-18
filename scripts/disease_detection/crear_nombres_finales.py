from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

IN_FILE = ROOT / "03_final" / "metadata" / "baseline_keep_with_ids.csv"
OUT_FILE = ROOT / "03_final" / "metadata" / "baseline_keep_with_filenames.csv"

rows = []

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames_in = reader.fieldnames
    for row in reader:
        ext = Path(row["original_filename"]).suffix.lower()
        if ext == "":
            ext = ".jpg"
        row["final_filename"] = f'{row["image_id"]}{ext}'
        rows.append(row)

fieldnames_out = fieldnames_in + ["final_filename"]

with open(OUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames_out)
    writer.writeheader()
    writer.writerows(rows)

print(f"CSV creado: {OUT_FILE}")
print(f"Filas exportadas: {len(rows)}")