import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
back = cv.imread('background.jpg')

while cap.isOpened():
    return_val, frame = cap.read()
    frame = np.flip(frame, axis=1)

    if return_val:
        # convert rgb to hsv
        hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # lower: hue-10,100,100 ; higher: hue+10,255,255 for RED!!
        red = np.uint8([[[0,0,255]]])
        hsv_red = cv.cvtColor(red, cv.COLOR_BGR2HSV) # [[[hue, saturation, value]]]
        # print(hsv_red)
        lower_red = np.array([0,100,100])
        upper_red = np.array([hsv_red[0,0,0]+10,255,255])

        # check if given array lies between upper and lower bound (is the pixel red?)
        mask = cv.inRange(hsv_frame, lower_red, upper_red)  
        cv.imshow('red_mask', mask)

        if cv.waitKey(1) & 0xFF==ord('q'):
            break

cap.release()
cv.destroyAllWindows()