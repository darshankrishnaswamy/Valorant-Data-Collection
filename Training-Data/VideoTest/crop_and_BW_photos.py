import cv2
import numpy as np
from PIL import Image

pog = cv2.imread("pog.jpg")
pog1 = cv2.imread("pog1.jpg")

img_grey = cv2.imread('pog.jpg', cv2.IMREAD_GRAYSCALE)
img_binary = cv2.threshold(img_grey, 230, 255, cv2.THRESH_BINARY)[1]

cv2.imwrite('test.jpg', img_binary)

img_grey = cv2.imread('pog1.jpg', cv2.IMREAD_GRAYSCALE)
img_binary = cv2.threshold(img_grey, 230, 255, cv2.THRESH_BINARY)[1]

cv2.imwrite('test1.jpg', img_binary)

test = cv2.imread("test.jpg")
test1 = cv2.imread("test1.jpg")

imga = test[210:235, 660:705]
imgb = test1[210:235, 660:705]

cv2.imwrite('test.jpg', imga)
cv2.imwrite('test1.jpg', imgb)

