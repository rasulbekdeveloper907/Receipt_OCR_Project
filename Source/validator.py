"""
validator.py

Validate SROIE 2019 dataset structure.

Author: Rasulbek Ruzmetov
Project: Receipt OCR
"""

from pathlib import Path


class DatasetValidator:
    """Validate SROIE 2019 dataset structure and file consistency."""

    REQUIRED_FOLDERS = ["img", "box", "entities"]

    def __init__(self, dataset_root: str):
        self.dataset_root = Path(dataset_root)

    def _check_folder(self, folder: Path):
        if not folder.exists():
            raise FileNotFoundError(f"Folder not found: {folder}")

    def _get_stem_set(self, folder: Path, extension: str):
        """
        Returns a set of file names without extension.
        Example:
            X0001.jpg -> X0001
            X0001.txt -> X0001
        """
        return {file.stem for file in folder.glob(f"*{extension}")}

    def validate_split(self, split: str):
        """
        Validate train or test dataset.
        """

        split_path = self.dataset_root / split

        self._check_folder(split_path)

        img_path = split_path / "img"
        box_path = split_path / "box"
        entity_path = split_path / "entities"

        self._check_folder(img_path)
        self._check_folder(box_path)
        self._check_folder(entity_path)

        images = self._get_stem_set(img_path, ".jpg")
        boxes = self._get_stem_set(box_path, ".txt")
        entities = self._get_stem_set(entity_path, ".txt")

        missing_box = sorted(images - boxes)
        missing_entity = sorted(images - entities)

        extra_box = sorted(boxes - images)
        extra_entity = sorted(entities - images)

        return {
            "images": len(images),
            "boxes": len(boxes),
            "entities": len(entities),
            "missing_box": missing_box,
            "missing_entity": missing_entity,
            "extra_box": extra_box,
            "extra_entity": extra_entity,
        }

    def validate(self):
        """
        Validate entire dataset.
        """

        print("=" * 55)
        print("        SROIE 2019 DATASET VALIDATION")
        print("=" * 55)

        overall_valid = True

        for split in ["train", "test"]:

            result = self.validate_split(split)

            print(f"\n[{split.upper()}]")

            print(f"Images   : {result['images']}")
            print(f"Boxes    : {result['boxes']}")
            print(f"Entities : {result['entities']}")

            if (
                result["missing_box"]
                or result["missing_entity"]
                or result["extra_box"]
                or result["extra_entity"]
            ):
                overall_valid = False

                print("\nStatus : INVALID")

                if result["missing_box"]:
                    print(f"Missing OCR Files : {len(result['missing_box'])}")

                if result["missing_entity"]:
                    print(f"Missing Entity Files : {len(result['missing_entity'])}")

                if result["extra_box"]:
                    print(f"Extra OCR Files : {len(result['extra_box'])}")

                if result["extra_entity"]:
                    print(f"Extra Entity Files : {len(result['extra_entity'])}")

            else:
                print("\nStatus : VALID")

        print("\n" + "=" * 55)

        if overall_valid:
            print("Dataset Status : VALID")
        else:
            print("Dataset Status : INVALID")

        print("=" * 55)