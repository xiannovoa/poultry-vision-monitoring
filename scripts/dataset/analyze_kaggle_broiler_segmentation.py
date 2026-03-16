import json
from pathlib import Path
from collections import defaultdict


def analyze_annotations(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)

    images = data["images"]
    annotations = data["annotations"]

    print("\n--- DATASET OVERVIEW ---")

    print(f"Number of images: {len(images)}")
    print(f"Number of annotations (chickens): {len(annotations)}")

    # Contar anotaciones por imagen
    annotations_per_image = defaultdict(int)

    for ann in annotations:
        annotations_per_image[ann["image_id"]] += 1

    counts = list(annotations_per_image.values())

    print("\n--- CHICKENS PER IMAGE ---")

    print(f"Images with annotations: {len(counts)}")
    print(f"Average chickens per image: {sum(counts)/len(counts):.2f}")
    print(f"Min chickens in image: {min(counts)}")
    print(f"Max chickens in image: {max(counts)}")

    # Analizar tamaño de bounding boxes
    bbox_areas = []

    for ann in annotations:
        _, _, w, h = ann["bbox"]
        bbox_areas.append(w * h)

    print("\n--- BOUNDING BOX STATS ---")

    print(f"Average bbox area: {sum(bbox_areas)/len(bbox_areas):.2f}")
    print(f"Min bbox area: {min(bbox_areas):.2f}")
    print(f"Max bbox area: {max(bbox_areas):.2f}")


if __name__ == "__main__":

    dataset_root = Path("data/01_raw/kaggle_broiler_segmentation/Json_Files")

    train_json = dataset_root / "traincoco.json"
    val_json = dataset_root / "valcoco.json"

    print("TRAIN DATASET")
    analyze_annotations(train_json)

    print("\nVALIDATION DATASET")
    analyze_annotations(val_json)