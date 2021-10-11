import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue,frame = capture.read()
    cv.imshow('Video',frame)
    #cv.imshow("Video 2", frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    if cv.waitKey(20) & 0xFF==ord('f'):
        frame = cv.flip(frame, 1)
    if cv.waitKey(20) & 0xFF==ord('a'):
        frame = cv.flip(frame, 0)   
    

capture.release()
cv.destroyAllWindows()