import numpy as np
import cv2
import sys

from scipy.linalg import norm
from scipy import sum, average

counter = 0

pog = cv2.imread("frame17719.jpg")
pog1 = cv2.imread("frame32190.jpg")

img_grey = cv2.imread('frame17719.jpg', cv2.IMREAD_GRAYSCALE)
img_binary = cv2.threshold(img_grey, 230, 255, cv2.THRESH_BINARY)[1]

img_grey1 = cv2.imread('frame32190.jpg', cv2.IMREAD_GRAYSCALE)
img_binary1 = cv2.threshold(img_grey1, 230, 255, cv2.THRESH_BINARY)[1]

imga_prior = img_binary[20:40, 620:665]
imgb_prior = img_binary1[20:40, 620:665]

imga = imga_prior/255
imgb = imgb_prior/255


def cos_distance(a, b):
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    dot_product = np.dot(a.flatten(), b.flatten())
    cos = dot_product / (a_norm * b_norm)
    return cos


print(cos_distance(imga, imgb))

if cos_distance(imga,imgb) > 0.9:
    cv2.imwrite('bigpog.jpg', imgb)

