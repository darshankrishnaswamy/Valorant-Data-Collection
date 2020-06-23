import cv2
from time import sleep

vidcap = cv2.VideoCapture('ValVideo.mp4')
count = 0
success = True
fps = int(vidcap.get(cv2.CAP_PROP_FPS))

while success:
    success,image = vidcap.read()
    print('read a new frame:',success)
    if count% fps == 0 :
        cv2.imwrite('./data/frame%d.jpg'%count,image)
        print('successfully written frame')
        sleep(0.8)
    count+=1

