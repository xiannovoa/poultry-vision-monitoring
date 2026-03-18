from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

IN_FILE = ROOT / "03_final" / "metadata" / "master_index_baseline_clean.csv"
OUT_FILE = ROOT / "03_final" / "metadata" / "baseline_keep_only.csv"

rows_out = []

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        if row["keep_drop_review"].strip().lower() == "keep":
            rows_out.append(row)

with open(OUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_out)

print(f"CSV creado: {OUT_FILE}")
print(f"Filas exportadas: {len(rows_out)}")