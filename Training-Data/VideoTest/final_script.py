from time import sleep

import numpy as np
import cv2
import pyautogui

vidcap = cv2.VideoCapture('ValVideo.mp4')
count = 0
success = True
fps = int(vidcap.get(cv2.CAP_PROP_FPS))

pog = cv2.imread("000_original_1080.jpg")
img_binary = cv2.threshold(pog, 230, 255, cv2.THRESH_BINARY)[1]

imga_prior = img_binary[28:65, 925:995]
imga = imga_prior / 255

imga_buy = img_binary[185:230, 820:1100] / 255

matchpog = cv2.imread("match_point.jpg")
img_binary_match = cv2.threshold(matchpog, 230, 255, cv2.THRESH_BINARY)[1]

a_mat = img_binary_match[185:215, 815:1110] / 255

switchpog = cv2.imread("last_round_b4_swap.jpg")
img_binary_switch = cv2.threshold(switchpog, 230, 255, cv2.THRESH_BINARY)[1]

a_sw = img_binary_switch[185:215, 670:1240] / 255

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
    # final_picture = imgb[15:440, 15:440]
    final_picture = imgb
    img_binary1 = cv2.threshold(imgb, 230, 255, cv2.THRESH_BINARY)[1]

    imgb_prior = img_binary1[28:65, 925:995]
    imgb = imgb_prior / 255

    imgb_buy = img_binary1[185:230, 820:1100] / 255
    b_sw = img_binary1[185:215, 670:1240] / 255
    b_mat = img_binary1[185:215, 815:1110] / 255
    # cv2.imshow("imga",imga)
    # cv2.imshow("imgb", imgb)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    if cos_distance(imga, imgb) > 0.95:
        if cos_distance(imga_buy, imgb_buy) >0.95 or cos_distance(a_mat, b_mat) > 0.95 or cos_distance(a_sw, b_sw)>0.95:
            print(cos_distance(imga, imgb))
            cv2.imwrite('./data/round%d.jpg' % count, final_picture)
            sleep(1)
            print('successfully written frame')
            count += 1
