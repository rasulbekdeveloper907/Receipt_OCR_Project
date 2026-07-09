"""
preprocessing.py

Receipt Image Preprocessing

Author : Rasulbek Ruzmetov
Project : Receipt OCR
"""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt


class ReceiptPreprocessor:

    def __init__(self):
        pass

    # --------------------------------------------------
    # Read Image
    # --------------------------------------------------

    def read_image(self, image_path):

        image = cv2.imread(str(image_path))

        if image is None:
            raise FileNotFoundError(image_path)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        return image

    # --------------------------------------------------
    # Save Image
    # --------------------------------------------------

    def save_image(self, image, save_path):

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        cv2.imwrite(str(save_path), image)

    # --------------------------------------------------
    # Show Image
    # --------------------------------------------------

    def show_image(self, image, title="Image"):

        plt.figure(figsize=(8,10))

        plt.imshow(image)

        plt.title(title)

        plt.axis("off")

        plt.show()

    # --------------------------------------------------
    # Resize
    # --------------------------------------------------

    def resize(
        self,
        image,
        width=None,
        height=None,
        interpolation=cv2.INTER_AREA
    ):

        h, w = image.shape[:2]

        if width is None and height is None:
            return image

        if width is None:

            ratio = height / h

            width = int(w * ratio)

        elif height is None:

            ratio = width / w

            height = int(h * ratio)

        resized = cv2.resize(
            image,
            (width, height),
            interpolation=interpolation
        )

        return resized

    # --------------------------------------------------
    # Convert to Gray
    # --------------------------------------------------

    def grayscale(self, image):

        return cv2.cvtColor(
            image,
            cv2.COLOR_RGB2GRAY
        )

    # --------------------------------------------------
    # Compare
    # --------------------------------------------------

    def compare(
        self,
        original,
        processed,
        title1="Original",
        title2="Processed"
    ):

        plt.figure(figsize=(15,8))

        plt.subplot(1,2,1)

        if len(original.shape)==2:
            plt.imshow(original,cmap="gray")
        else:
            plt.imshow(original)

        plt.title(title1)

        plt.axis("off")

        plt.subplot(1,2,2)

        if len(processed.shape)==2:
            plt.imshow(processed,cmap="gray")
        else:
            plt.imshow(processed)

        plt.title(title2)

        plt.axis("off")

        plt.show()