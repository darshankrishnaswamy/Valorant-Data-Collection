import numpy as np
import cv2
import pyautogui

vidcap = cv2.VideoCapture('ValVideo.mp4')
count = 0
success = True
fps = int(vidcap.get(cv2.CAP_PROP_FPS))

pog = cv2.imread("000_laptop.jpg")
img_binary = cv2.threshold(pog, 230, 255, cv2.THRESH_BINARY)[1]

imga_prior = img_binary[28:65, 925:995]
imga = imga_prior / 255


def cos_distance(a, b):
    if np.count_nonzero(a) == 0:
        return 0
    if np.count_nonzero(b) == 0:
        return 0
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    dot_product = np.dot(a.flatten(), b.flatten())
    cos = dot_product / (a_norm * b_norm)
    return cos


while success:
    imgb = pyautogui.screenshot()
    imgb = cv2.cvtColor(np.array(imgb), cv2.COLOR_RGB2BGR)
    final_picture = imgb
    img_binary1 = cv2.threshold(imgb, 230, 255, cv2.THRESH_BINARY)[1]

    imgb_prior = img_binary1[28:65, 925:995]
    imgb = imgb_prior / 255
    # cv2.imshow("imga",imga)
    # cv2.imshow("imgb", imgb)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    if cos_distance(imga, imgb) > 0.95:
        print(cos_distance(imga, imgb))
        cv2.imwrite('./data/frame%d.jpg' % count, final_picture)
        print('successfully written frame')
    count += 1

