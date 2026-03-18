from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

IN_FILE = ROOT / "03_final" / "metadata" / "baseline_keep_only.csv"
OUT_FILE = ROOT / "03_final" / "metadata" / "baseline_keep_with_ids.csv"

rows = []

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames_in = reader.fieldnames
    for row in reader:
        rows.append(row)

rows_sorted = sorted(
    rows,
    key=lambda r: (
        r["final_label"].strip(),
        r["source_id"].strip(),
        r["original_filename"].strip().lower(),
    )
)

for i, row in enumerate(rows_sorted, start=1):
    row["image_id"] = f"CFD_{i:05d}"

fieldnames_out = ["image_id"] + fieldnames_in

with open(OUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames_out)
    writer.writeheader()
    writer.writerows(rows_sorted)

print(f"CSV creado: {OUT_FILE}")
print(f"Filas exportadas: {len(rows_sorted)}")