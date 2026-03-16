import os
import shutil
import csv
from pathlib import Path

# rutas
RAW_DATASET = Path("data/01_raw/mendeley_broiler_weight")
OUTPUT_DIR = Path("data/02_work/mendeley_broiler_weight_dataset")
IMAGES_DIR = OUTPUT_DIR / "images"
LABELS_FILE = OUTPUT_DIR / "labels.csv"

# crear carpetas si no existen
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

rows = []

image_id = 0

# recorrer carpetas de peso
for weight_folder in sorted(RAW_DATASET.iterdir()):

    if not weight_folder.is_dir():
        continue

    weight = weight_folder.name

    for img_path in weight_folder.glob("*.jpg"):

        image_id += 1

        new_name = f"img_{image_id:05d}.jpg"
        new_path = IMAGES_DIR / new_name

        shutil.copy(img_path, new_path)

        rows.append([new_name, weight])


# guardar labels.csv
with open(LABELS_FILE, "w", newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["image", "weight"])

    for row in rows:
        writer.writerow(row)


print("Dataset preparado correctamente")
print(f"Total imágenes: {len(rows)}")
print(f"Guardado en: {OUTPUT_DIR}")