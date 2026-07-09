"""
explorer.py

Dataset Explorer for SROIE 2019
"""

from pathlib import Path
from PIL import Image
import json


class DatasetExplorer:

    def __init__(self, dataset):

        self.dataset = dataset

    def image_statistics(self):

        widths = []
        heights = []

        for sample in self.dataset:

            image = Image.open(sample["image_path"])

            w, h = image.size

            widths.append(w)
            heights.append(h)

        print("=" * 60)
        print("IMAGE STATISTICS")
        print("=" * 60)

        print(f"Total Images : {len(widths)}")
        print(f"Min Width    : {min(widths)}")
        print(f"Max Width    : {max(widths)}")
        print(f"Average Width: {sum(widths)/len(widths):.2f}")

        print()

        print(f"Min Height   : {min(heights)}")
        print(f"Max Height   : {max(heights)}")
        print(f"Average Height: {sum(heights)/len(heights):.2f}")

    def entity_statistics(self):

        print("=" * 60)
        print("ENTITY STATISTICS")
        print("=" * 60)

        total_company = 0
        total_address = 0
        total_date = 0
        total_total = 0

        for sample in self.dataset:

            with open(sample["entity_path"], encoding="utf-8") as f:

                entity = json.load(f)

            if entity["company"]:
                total_company += 1

            if entity["address"]:
                total_address += 1

            if entity["date"]:
                total_date += 1

            if entity["total"]:
                total_total += 1

        print(f"Company : {total_company}")
        print(f"Address : {total_address}")
        print(f"Date    : {total_date}")
        print(f"Total   : {total_total}")      

    def ocr_statistics(self):

        print("=" * 60)
        print("OCR STATISTICS")
        print("=" * 60)

        total_lines = 0

        max_lines = 0
        min_lines = 100000

        for sample in self.dataset:

            with open(sample["box_path"], encoding="utf8") as f:

                lines = f.readlines()

            total_lines += len(lines)

            max_lines = max(max_lines, len(lines))
            min_lines = min(min_lines, len(lines))

        print(f"Average OCR Lines : {total_lines/len(self.dataset):.2f}")
        print(f"Max OCR Lines     : {max_lines}")
        print(f"Min OCR Lines     : {min_lines}")

    def summary(self):

        self.image_statistics()

        print()

        self.entity_statistics()

        print()

        self.ocr_statistics()                