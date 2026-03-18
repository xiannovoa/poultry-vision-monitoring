from pathlib import Path
import csv
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index_hashed.csv"

hashes = []

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        hashes.append(row["sha256"].strip())

counter = Counter(hashes)

num_hashes_repetidos = sum(1 for h, n in counter.items() if n > 1)
num_imagenes_en_grupos_repetidos = sum(n for h, n in counter.items() if n > 1)
num_duplicados_sobrantes = sum(n - 1 for h, n in counter.items() if n > 1)

print(f"Hashes repetidos: {num_hashes_repetidos}")
print(f"Imagenes dentro de grupos repetidos: {num_imagenes_en_grupos_repetidos}")
print(f"Duplicados exactos sobrantes: {num_duplicados_sobrantes}")