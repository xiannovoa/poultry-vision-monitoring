from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "casos_fuertes_multifuente.csv"
OUT_FILE = INV / "decisiones_solapamiento_src02.csv"

rows_out = []

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        source_id = row["source_id"].strip()

        if source_id == "src02_poultry":
            action = "drop"
            reason = "strong_multisource_overlap_keep_src01"
        else:
            action = "keep"
            reason = "strong_multisource_overlap_keep_src01"

        rows_out.append({
            "final_label": row["final_label"],
            "original_filename": row["original_filename"],
            "phash": row["phash"],
            "source_id": source_id,
            "raw_split_or_folder": row["raw_split_or_folder"],
            "raw_path": row["raw_path"],
            "overlap_action": action,
            "overlap_reason": reason,
        })

with open(OUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "final_label",
            "original_filename",
            "phash",
            "source_id",
            "raw_split_or_folder",
            "raw_path",
            "overlap_action",
            "overlap_reason",
        ],
    )
    writer.writeheader()
    writer.writerows(rows_out)

print(f"CSV creado: {OUT_FILE}")
print(f"Filas exportadas: {len(rows_out)}")