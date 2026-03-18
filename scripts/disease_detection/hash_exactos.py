from pathlib import Path
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index_checked.csv"
OUT_FILE = INV / "master_index_hashed.csv"

def sha256_file(path, chunk_size=1024 * 1024):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

rows = []

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        raw_path = Path(row["raw_path"])
        row["sha256"] = sha256_file(raw_path)
        rows.append(row)

fieldnames = list(rows[0].keys())

with open(OUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"CSV creado: {OUT_FILE}")
print(f"Total filas: {len(rows)}")