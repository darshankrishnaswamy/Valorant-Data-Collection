from time import sleep

import numpy as np
import cv2
import pyautogui

vidcap = cv2.VideoCapture('ValVideo.mp4')
count = 0
success = True
fps = int(vidcap.get(cv2.CAP_PROP_FPS))

signal = True

count = 1

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

endpog = cv2.imread("end.jpg")
img_binary_end = cv2.threshold(endpog, 230, 255, cv2.THRESH_BINARY)[1]

a_end = img_binary_end[165:230, 830:1070] / 255


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
    b_end = img_binary1[165:230, 830:1070] / 255

    name = './data/fullgameJune25/round' + str(count) + '.jpg'
    if cos_distance(imga, imgb) > 0.92:
        if cos_distance(imga_buy, imgb_buy) > 0.92 or \
                cos_distance(a_mat, b_mat) > 0.92 or \
                cos_distance(a_sw, b_sw) > 0.92 or \
                cos_distance(a_end, b_end) > 0.92:
            print(cos_distance(imga, imgb))
            cv2.imwrite(name, final_picture)
            print('successfully written frame')
            sleep(2)
            count += 1
            signal = False

    if count > 2 and signal == False:
        name_alt = './data/fullgameJune25/round' + str(count-2) + '.jpg'
        pogbehind = cv2.imread(name_alt)
        behind = cv2.threshold(pogbehind, 230, 255, cv2.THRESH_BINARY)[1][35:65, 810:835]/255
        current = cv2.threshold(final_picture, 230, 255, cv2.THRESH_BINARY)[1][35:65, 810:835]/255
        if cos_distance(current, behind) < 0.9:
            print('won')
        else:
            print('lost')
        print(cos_distance(current, behind))
        signal = True

