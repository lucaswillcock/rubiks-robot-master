import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue,frame = capture.read()
    frame = cv.flip(frame, 1)
    cv.imshow('Video',frame)
    #cv.imshow("Video 2", frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()