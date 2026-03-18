from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

SRC_DIR = ROOT / "01_raw" / "src01_main" / "Train"
CSV_IN = ROOT / "01_raw" / "src01_main" / "train_data.csv"

OUT_DIR = ROOT / "02_work" / "inventory"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_CSV = OUT_DIR / "src01_main_index.csv"

label_map = {
    "Healthy": "healthy",
    "Coccidiosis": "coccidiosis",
    "Salmonella": "salmonella",
    "New Castle Disease": "newcastle",
}

rows = []

with open(CSV_IN, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        original_filename = row["images"].strip()
        original_label = row["label"].strip()

        final_label = label_map.get(original_label, "")

        rows.append({
            "source_id": "src01_main",
            "raw_split_or_folder": "Train",
            "original_filename": original_filename,
            "original_label": original_label,
            "final_label": final_label,
            "keep_drop_review": "keep",
            "notes": ""
        })

with open(OUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
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

print(f"CSV creado: {OUT_CSV}")
print(f"Total filas: {len(rows)}")