#convert videos to images
import cv2
import os
vidcap = cv2.VideoCapture("putvideofilenamehere.mp4")
count=0
while True:
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite("{:d}.png".format(count), image)
        count += 1
