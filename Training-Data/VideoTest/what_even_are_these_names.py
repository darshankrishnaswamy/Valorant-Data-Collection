from PIL import Image
from PIL import ImageChops
import cv2

im1 = Image.open("bruh.jpg")
im2 = Image.open("bruh1.jpg")

diff = ImageChops.difference(im2, im1)

diff.show()

