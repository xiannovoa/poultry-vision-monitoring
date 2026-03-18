from pathlib import Path
import csv
from PIL import Image
import imagehash

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "02_work" / "inventory"

IN_FILE = INV / "master_index_dedup_exact.csv"
OUT_FILE = INV / "master_index_phash.csv"

rows = []

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["keep_drop_review"].strip().lower() != "keep":
            rows.append(row)
            continue

        raw_path = Path(row["raw_path"])

        with Image.open(raw_path) as img:
            ph = str(imagehash.phash(img))

        row["phash"] = ph
        rows.append(row)

fieldnames = list(rows[0].keys())
if "phash" not in fieldnames:
    fieldnames.append("phash")

with open(OUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"CSV creado: {OUT_FILE}")
print(f"Total filas: {len(rows)}")