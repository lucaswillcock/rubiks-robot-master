import cv2 as cv
import numpy as np
capture = cv.VideoCapture(0)

while True:
    isTrue,frame = capture.read()
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_blue = np.array([60, 35, 140])
    upper_blue = np.array([180, 255, 255])
    
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    
    frame = cv.bitwise_and(frame, frame, mask = mask)
    
    frame = cv.flip(frame, 1)
    #frame = cv.rectangle(frame, (20,20), (120, 120), (0, 0, 0))
    #frame = cv.Canny(frame, 100, 100)
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    

capture.release()
cv.destroyAllWindows()