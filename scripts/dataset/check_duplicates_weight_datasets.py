from pathlib import Path
from PIL import Image
import imagehash

# rutas de datasets preparados
MENDELEY_DIR = Path("data/02_work/mendeley_broiler_weight_dataset/images")
ROBOFLOW_DIR = Path("data/02_work/roboflow_broiler_weight_dataset/images")

# umbral de similitud (0 = idénticas)
HASH_THRESHOLD = 5


def compute_hashes(image_dir):
    """
    Calcula hash perceptual de todas las imágenes
    """
    hashes = {}

    for img_path in image_dir.glob("*.jpg"):
        try:
            img = Image.open(img_path)
            phash = imagehash.phash(img)

            hashes[img_path] = phash

        except Exception as e:
            print(f"Error leyendo {img_path}: {e}")

    return hashes


print("Calculando hashes Mendeley...")
mendeley_hashes = compute_hashes(MENDELEY_DIR)

print("Calculando hashes Roboflow...")
roboflow_hashes = compute_hashes(ROBOFLOW_DIR)


print("\nComparando imágenes...")

duplicates = []

for m_path, m_hash in mendeley_hashes.items():

    for r_path, r_hash in roboflow_hashes.items():

        distance = m_hash - r_hash

        if distance <= HASH_THRESHOLD:

            duplicates.append((m_path, r_path, distance))


print("RESULTADOS")

print(f"Imágenes Mendeley: {len(mendeley_hashes)}")
print(f"Imágenes Roboflow: {len(roboflow_hashes)}")
print(f"Posibles duplicados encontrados: {len(duplicates)}")


# mostrar algunos ejemplos
print("\nEjemplos de duplicados detectados:\n")

for m, r, d in duplicates[:10]:
    print(f"dist={d}")
    print(f"Mendeley : {m}")
    print(f"Roboflow : {r}")
    print()