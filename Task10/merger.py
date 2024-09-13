import os
import cv2
from PIL import Image, ImageDraw
import numpy as np
import re

def detect_dot(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 250, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None, None
    dot_contour = max(contours, key=cv2.contourArea)
    M = cv2.moments(dot_contour)
    if M["m00"] == 0:
        return None, None
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    dot_color = image[cY, cX]  # BGR format
    dot_color = (dot_color[2], dot_color[1], dot_color[0])
    
    return (cX, cY), dot_color

def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')

folder_path = "/Users/karthikprathipati/Desktop/amFOSS-Tasks/Task10/assets"
images = sorted(
    [os.path.join(folder_path, img) for img in os.listdir(folder_path) if img.endswith('.png')],
    key=lambda x: extract_number(os.path.basename(x))
)
prev_position = None
prev_color = None

canvas_size = (512, 512)
canvas = Image.new('RGB', canvas_size, (255, 255, 255))
draw = ImageDraw.Draw(canvas)

for image_path in images:
    position, color = detect_dot(image_path)
    
    if position is None and color is None:
        prev_position = None
        continue

    if prev_position and position:
        draw.line([prev_position, position], fill=prev_color, width=3)
    
    prev_position = position
    prev_color = color

canvas.save("stitched_message.png")
print("Stitched image saved as 'stitched_message.png'.")
