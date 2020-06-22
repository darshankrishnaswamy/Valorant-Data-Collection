import cv2

img_grey = cv2.imread('pog.jpg', cv2.IMREAD_GRAYSCALE)
img_binary = cv2.threshold(img_grey, 175, 255, cv2.THRESH_BINARY)[1]

cv2.imwrite('test.jpg',img_binary)

