from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

IN_FILE = ROOT / "03_final" / "metadata" / "baseline_keep_with_filenames.csv"
OUT_FILE = ROOT / "03_final" / "labels.csv"

rows_out = []

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows_out.append({
            "image_id": row["image_id"],
            "filename": row["final_filename"],
            "label": row["final_label"],
        })

with open(OUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["image_id", "filename", "label"],
    )
    writer.writeheader()
    writer.writerows(rows_out)

print(f"CSV creado: {OUT_FILE}")
print(f"Filas exportadas: {len(rows_out)}")