import logging

import cv2
import imutils
import numpy as np
import requests

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

url = [
    'https://i.imgur.com/sjVZKOo.jpg',
    'https://i.imgur.com/6UihTbh.jpg',
    'https://i.imgur.com/txRM3L7.jpg',
    'https://i.imgur.com/enU5kd4.jpg',
    'https://i.imgur.com/lgzUGRe.jpg'
]

images = []

for u in url:
    response = requests.get(u, stream=True).raw
    image = np.asarray(bytearray(response.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    images.append(image)

stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
stitched = stitcher.stitch(images)
cv2.imwrite("out.jpg", stitched[1])
