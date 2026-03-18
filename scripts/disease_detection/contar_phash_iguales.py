from pathlib import Path
import csv
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index_phash.csv"

phashes = []

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["keep_drop_review"].strip().lower() == "keep":
            ph = row.get("phash", "").strip()
            if ph:
                phashes.append(ph)

counter = Counter(phashes)

num_phash_repetidos = sum(1 for _, n in counter.items() if n > 1)
num_imagenes_en_grupos = sum(n for _, n in counter.items() if n > 1)
num_sobrantes = sum(n - 1 for _, n in counter.items() if n > 1)

print(f"pHash repetidos: {num_phash_repetidos}")
print(f"Imagenes dentro de grupos pHash repetidos: {num_imagenes_en_grupos}")
print(f"Sobrantes potenciales: {num_sobrantes}")