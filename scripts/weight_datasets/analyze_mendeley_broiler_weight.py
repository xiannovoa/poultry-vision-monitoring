import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

LABELS_FILE = Path("data/02_work/mendeley_broiler_weight_dataset/labels.csv")

df = pd.read_csv(LABELS_FILE)

print("Número total de imágenes:", len(df))
print("Peso mínimo:", df["weight"].min())
print("Peso máximo:", df["weight"].max())
print("Número de pesos únicos:", df["weight"].nunique())

# distribución de pesos
plt.hist(df["weight"], bins=30)
plt.xlabel("Peso (g)")
plt.ylabel("Número de imágenes")
plt.title("Distribución de pesos en el dataset")
plt.show()