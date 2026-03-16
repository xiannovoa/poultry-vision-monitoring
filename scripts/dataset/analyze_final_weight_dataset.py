import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# rutas del dataset final
DATASET_DIR = Path("data/03_final/broiler_weight_dataset")
LABELS_FILE = DATASET_DIR / "labels.csv"


def analyze_dataset():

    # cargar etiquetas
    df = pd.read_csv(LABELS_FILE)

    weights = df["weight"]

    print("DATASET FINAL - ESTADÍSTICAS")

    print(f"Número total de imágenes: {len(weights)}")
    print(f"Peso mínimo: {weights.min()} g")
    print(f"Peso máximo: {weights.max()} g")
    print(f"Número de pesos únicos: {weights.nunique()}")

    print("\nESTADÍSTICAS DESCRIPTIVAS")

    print(weights.describe())

    # histograma
    plt.figure(figsize=(10,6))

    plt.hist(weights, bins=40)

    plt.title("Distribución de pesos en el dataset final")
    plt.xlabel("Peso (g)")
    plt.ylabel("Número de imágenes")

    plt.show()


if __name__ == "__main__":
    analyze_dataset()