from pathlib import Path
import csv
import shutil
from PIL import Image
import imagehash

# datasets preparados
MENDELEY_IMAGES = Path("data/02_work/mendeley_broiler_weight_dataset/images")
MENDELEY_LABELS = Path("data/02_work/mendeley_broiler_weight_dataset/labels.csv")

ROBOFLOW_IMAGES = Path("data/02_work/roboflow_broiler_weight_dataset/images")
ROBOFLOW_LABELS = Path("data/02_work/roboflow_broiler_weight_dataset/labels.csv")

# dataset final
FINAL_DIR = Path("data/03_final/broiler_weight_dataset")
FINAL_IMAGES = FINAL_DIR / "images"
FINAL_LABELS = FINAL_DIR / "labels.csv"

FINAL_IMAGES.mkdir(parents=True, exist_ok=True)

HASH_THRESHOLD = 5


def load_labels(csv_path):
    labels = {}
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            labels[row["image"]] = int(row["weight"])
    return labels


def compute_hash(image_path):
    img = Image.open(image_path)
    return imagehash.phash(img)


print("Cargando etiquetas...")
mendeley_labels = load_labels(MENDELEY_LABELS)
roboflow_labels = load_labels(ROBOFLOW_LABELS)

print("Procesando imágenes Mendeley...")

hashes = []
rows = []
image_id = 0

for img_name, weight in mendeley_labels.items():

    img_path = MENDELEY_IMAGES / img_name
    h = compute_hash(img_path)

    hashes.append(h)

    new_name = f"img_{image_id:05d}.jpg"
    shutil.copy(img_path, FINAL_IMAGES / new_name)

    rows.append([new_name, weight])
    image_id += 1


print("Procesando imágenes Roboflow...")

duplicates = 0

for img_name, weight in roboflow_labels.items():

    img_path = ROBOFLOW_IMAGES / img_name
    h = compute_hash(img_path)

    duplicate = False

    for existing in hashes:
        if h - existing <= HASH_THRESHOLD:
            duplicate = True
            break

    if duplicate:
        duplicates += 1
        continue

    hashes.append(h)

    new_name = f"img_{image_id:05d}.jpg"
    shutil.copy(img_path, FINAL_IMAGES / new_name)

    rows.append([new_name, weight])
    image_id += 1


print("\nGuardando labels...")

with open(FINAL_LABELS, "w", newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["image", "weight"])
    writer.writerows(rows)


print("DATASET FINAL GENERADO")

print(f"Imágenes finales: {image_id}")
print(f"Duplicados eliminados: {duplicates}")
print(f"Guardado en: {FINAL_DIR}")