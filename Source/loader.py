"""
loader.py

Load SROIE 2019 dataset.

Author: Rasulbek Ruzmetov
Project: Receipt OCR
"""

from pathlib import Path
from typing import List, Dict


class DatasetLoader:
    """
    Load SROIE 2019 dataset.
    """

    def __init__(self, dataset_root: str):

        self.dataset_root = Path(dataset_root)

    def load_split(self, split: str = "train") -> List[Dict]:

        split_path = self.dataset_root / split

        img_dir = split_path / "img"
        box_dir = split_path / "box"
        entity_dir = split_path / "entities"

        image_files = sorted(img_dir.glob("*.jpg"))

        dataset = []

        for image_path in image_files:

            file_name = image_path.stem

            box_path = box_dir / f"{file_name}.txt"
            entity_path = entity_dir / f"{file_name}.txt"

            dataset.append(
                {
                    "id": file_name,
                    "image_path": image_path,
                    "box_path": box_path,
                    "entity_path": entity_path,
                }
            )

        return dataset

    def load_train(self):

        return self.load_split("train")

    def load_test(self):

        return self.load_split("test")