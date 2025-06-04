import cv2
import numpy as np
from PIL import Image

def segment_rooftop(image: Image.Image):
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    mask = np.zeros_like(gray)
    cv2.drawContours(mask, contours, -1, 255, -1)

    usable_area_px = cv2.countNonZero(mask)
    total_px = gray.size
    percent_usable = usable_area_px / total_px * 100

    return Image.fromarray(mask), percent_usable
