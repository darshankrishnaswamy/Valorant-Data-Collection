import cv2

vidcap = cv2.VideoCapture('ValVideo.mp4')
count = 0
success = True
fps = int(vidcap.get(cv2.CAP_PROP_FPS))

while success:
    success,image = vidcap.read()
    print('read a new frame:',success)
    if count%(fps*0.5) == 0 :
         cv2.imwrite('./data/frame%d.jpg'%count,image)
         print('successfully written frame')
    count+=1

