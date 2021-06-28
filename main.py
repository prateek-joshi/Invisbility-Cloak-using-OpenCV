import cv2 as cv
import numpy as np

video_capture = cv.VideoCapture(0)

while video_capture.isOpened():
    return_val, img = video_capture.read()
    cv.imshow("Invisibility", np.flip(img, axis=1))
    if cv.waitKey(10)==27:
        break