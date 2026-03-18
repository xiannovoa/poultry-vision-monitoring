from pathlib import Path
import csv
import shutil

ROOT = Path(__file__).resolve().parents[1]

IN_FILE = ROOT / "03_final" / "metadata" / "baseline_keep_with_filenames.csv"
OUT_DIR = ROOT / "03_final" / "images"

OUT_DIR.mkdir(parents=True, exist_ok=True)

count = 0

with open(IN_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        src = Path(row["raw_path"])
        dst = OUT_DIR / row["final_filename"]
        shutil.copy2(src, dst)
        count += 1

print(f"Imagenes copiadas: {count}")
print(f"Carpeta destino: {OUT_DIR}")