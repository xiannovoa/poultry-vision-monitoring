from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

MASTER_IN = INV / "master_index_hashed.csv"
DUP_IN = INV / "decisiones_duplicados_exactos.csv"
MASTER_OUT = INV / "master_index_dedup_exact.csv"

# Cargamos las decisiones de duplicados exactos
drop_map = {}

with open(DUP_IN, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        key = (
            row["source_id"].strip(),
            row["raw_split_or_folder"].strip(),
            row["original_filename"].strip(),
        )
        drop_map[key] = row["duplicate_action"].strip().lower()

rows_out = []

with open(MASTER_IN, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames.copy()

    for row in reader:
        key = (
            row["source_id"].strip(),
            row["raw_split_or_folder"].strip(),
            row["original_filename"].strip(),
        )

        action = drop_map.get(key, None)

        if action == "drop":
            row["keep_drop_review"] = "drop"
            if row["notes"].strip():
                row["notes"] += "; exact_duplicate"
            else:
                row["notes"] = "exact_duplicate"

        rows_out.append(row)

with open(MASTER_OUT, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_out)

print(f"CSV creado: {MASTER_OUT}")
print(f"Total filas: {len(rows_out)}")