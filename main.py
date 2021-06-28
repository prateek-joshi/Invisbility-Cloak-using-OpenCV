import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
background = cv.imread('background.jpg')

while cap.isOpened():
    return_val, frame = cap.read()
    # frame = np.flip(frame, axis=1)

    if return_val:
        # convert rgb to hsv
        hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # lower: hue-10,100,100 ; higher: hue+10,255,255 for RED!!
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])

        # check if given array lies between upper and lower bound (is the pixel blue?)
        # all things blue
        mask = cv.inRange(hsv_frame, lower_blue, upper_blue)
        part1 = cv.bitwise_and(background,background,mask=mask)

        # all things not blue
        not_mask = cv.bitwise_not(mask)
        part2 = cv.bitwise_and(frame,frame,mask=not_mask)
        cv.imshow("part2",part1+part2)

        if cv.waitKey(1) & 0xFF==ord('q'):
            break

cap.release()
cv.destroyAllWindows()