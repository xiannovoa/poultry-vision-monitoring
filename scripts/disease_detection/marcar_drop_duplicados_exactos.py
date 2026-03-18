from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "duplicados_exactos.csv"
OUT_FILE = INV / "decisiones_duplicados_exactos.csv"

rows_out = []

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        suggested_keep = row["suggested_keep"].strip().lower()

        rows_out.append({
            "sha256": row["sha256"],
            "source_id": row["source_id"],
            "raw_split_or_folder": row["raw_split_or_folder"],
            "original_filename": row["original_filename"],
            "final_label": row["final_label"],
            "raw_path": row["raw_path"],
            "duplicate_action": "keep" if suggested_keep == "yes" else "drop",
            "duplicate_reason": "exact_duplicate",
        })

with open(OUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "sha256",
            "source_id",
            "raw_split_or_folder",
            "original_filename",
            "final_label",
            "raw_path",
            "duplicate_action",
            "duplicate_reason",
        ],
    )
    writer.writeheader()
    writer.writerows(rows_out)

print(f"CSV creado: {OUT_FILE}")
print(f"Filas exportadas: {len(rows_out)}")