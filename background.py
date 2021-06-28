"""
Stores the background image as a jpg file
"""
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)    # webcam
while cap.isOpened():
    return_val, background = cap.read()
    background = np.flip(background, axis=1)
    if return_val:
        cv.imshow('background',background)
        if cv.waitKey(5) == ord('q'):   # gives unicode value of 'q'
            # save the image
            cv.imwrite('background.jpg',background)
            break

cap.release()
cv.destroyAllWindows()
            