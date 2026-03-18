from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

IMAGES_DIR = ROOT / "03_final" / "images"
LABELS_FILE = ROOT / "03_final" / "labels.csv"
SOURCES_FILE = ROOT / "03_final" / "sources.csv"

image_files = [p.name for p in IMAGES_DIR.iterdir() if p.is_file()]
num_images = len(image_files)

with open(LABELS_FILE, "r", encoding="utf-8-sig", newline="") as f:
    num_labels = sum(1 for _ in csv.DictReader(f))

with open(SOURCES_FILE, "r", encoding="utf-8-sig", newline="") as f:
    num_sources = sum(1 for _ in csv.DictReader(f))

print(f"imagenes_en_carpeta: {num_images}")
print(f"filas_labels: {num_labels}")
print(f"filas_sources: {num_sources}")