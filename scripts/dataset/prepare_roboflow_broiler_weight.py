import shutil
import csv
import re
from pathlib import Path

# rutas
RAW_DATASET = Path("data/01_raw/roboflow_broiler_weight")
OUTPUT_DIR = Path("data/02_work/roboflow_broiler_weight_dataset")

IMAGES_DIR = OUTPUT_DIR / "images"
LABELS_FILE = OUTPUT_DIR / "labels.csv"

# crear carpetas si no existen
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

rows = []
image_id = 0

# regex para extraer peso
# ejemplo filename: 140_139-5.jpg
weight_pattern = re.compile(r"\d+_(\d+)-")

# recorrer splits
for split in ["train", "valid", "test"]:

    split_dir = RAW_DATASET / split

    if not split_dir.exists():
        continue

    for img_path in split_dir.rglob("*.jpg"):

        filename = img_path.name

        # extraer peso
        match = weight_pattern.search(filename)

        if not match:
            print(f"Peso no encontrado en {filename}")
            continue

        weight = int(match.group(1))

        # nuevo nombre imagen
        new_name = f"img_{image_id:05d}.jpg"
        new_path = IMAGES_DIR / new_name

        # copiar imagen
        shutil.copy(img_path, new_path)

        rows.append([new_name, weight])

        image_id += 1


# guardar labels.csv
with open(LABELS_FILE, "w", newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["image", "weight"])

    writer.writerows(rows)


print("Dataset preparado correctamente")
print(f"Total imágenes: {image_id}")
print(f"Guardado en: {OUTPUT_DIR}")