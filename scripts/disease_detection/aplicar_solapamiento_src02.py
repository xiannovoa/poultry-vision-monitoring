from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

MASTER_IN = INV / "master_index_phash.csv"
DECISIONS_IN = INV / "decisiones_solapamiento_src02.csv"
MASTER_OUT = INV / "master_index_dedup_multisource.csv"

drop_map = {}

with open(DECISIONS_IN, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        key = (
            row["source_id"].strip(),
            row["raw_split_or_folder"].strip(),
            Path(row["raw_path"].strip()).name,
        )
        drop_map[key] = (
            row["overlap_action"].strip().lower(),
            row["overlap_reason"].strip(),
        )

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

        decision = drop_map.get(key)

        if decision is not None:
            action, reason = decision
            if action == "drop":
                row["keep_drop_review"] = "drop"
                if row["notes"].strip():
                    row["notes"] += f"; {reason}"
                else:
                    row["notes"] = reason

        rows_out.append(row)

with open(MASTER_OUT, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_out)

print(f"CSV creado: {MASTER_OUT}")
print(f"Total filas: {len(rows_out)}")