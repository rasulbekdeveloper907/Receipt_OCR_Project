"""
visualizer.py

Visualize SROIE 2019 receipts.
"""

import cv2
import matplotlib.pyplot as plt


class ReceiptVisualizer:

    def __init__(self, dataset):

        self.dataset = dataset

    # ----------------------------------------------------
    # Show Image
    # ----------------------------------------------------

    def show_image(self, index=0):

        sample = self.dataset[index]

        image = cv2.imread(str(sample["image_path"]))

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        plt.figure(figsize=(8,10))
        plt.imshow(image)
        plt.axis("off")
        plt.title(sample["id"])

        plt.show()