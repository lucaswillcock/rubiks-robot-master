import cv2 as cv
import numpy as np
capture0 = cv.VideoCapture(0)
#capture1 = cv.VideoCapture(1)

while True:
    isTrue,frame = capture0.read()
    #isTrue,frame1 = capture1.read()
    
    #hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #lower_blue = np.array([60, 35, 140])
    #upper_blue = np.array([180, 255, 255])
    
    #mask = cv.inRange(hsv, lower_blue, upper_blue)
    
    #frame = cv.bitwise_and(frame, frame, mask = mask)
    
    frame = cv.flip(frame, -1)
    #frame1 = cv.flip(frame1, 1)
    #frame = cv.rectangle(frame, (20,20), (120, 120), (0, 0, 0))
    #frame = cv.Canny(frame, 100, 100)
    cv.imshow('Video',frame)
    #cv.imshow("cam 2", frame1)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    

capture0.release()
cv.destroyAllWindows()