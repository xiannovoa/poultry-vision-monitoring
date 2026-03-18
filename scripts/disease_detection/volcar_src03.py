from pathlib import Path
import csv

# Ruta base del proyecto
ROOT = Path(__file__).resolve().parents[1]

# Carpeta de entrada
SRC = ROOT / "01_raw" / "src03_extra"

# Carpeta de salida
OUT_DIR = ROOT / "02_work" / "inventory"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_CSV = OUT_DIR / "src03_extra_index.csv"

rows = []

label_map = {
    "Coccidiosis": "coccidiosis",
    "Healthy": "healthy",
}

for folder_name, final_label in label_map.items():
    folder = SRC / folder_name
    if not folder.exists():
        print(f"No existe la carpeta: {folder}")
        continue

    for img_path in sorted(folder.iterdir()):
        if img_path.is_file():
            rows.append({
                "source_id": "src03_extra",
                "raw_split_or_folder": folder_name,
                "original_filename": img_path.name,
                "original_label": folder_name,
                "final_label": final_label,
                "keep_drop_review": "keep",
                "notes": ""
            })

with open(OUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
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