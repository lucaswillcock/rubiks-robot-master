import cv2 as cv
import numpy as np
import imutils

#image parameters
startRef = (180, 370)

startRefx = 185
startRefy = 368

truePixelLength = 240
perspectiveLength = 196

xIncrement = 207
yIncrement = 130

#process image
cubeBottomRight = cv.imread("cube.jpeg")
cubeBottomRight = imutils.rotate(cubeBottomRight, -0.4)
cubeBottomRight = cv.circle(cubeBottomRight, startRef, 10, (250, 0, 0), 20)
cubeBottomRight = cv.circle(cubeBottomRight, (350, 468), 10, (250, 0, 0), 20)

x = startRefx
y = startRefy
for i in range(4):
    for i in range(4):
        cubeBottomRight = cv.circle(cubeBottomRight, (x, y), 10, (250, 0, 0), 20)
        x += xIncrement * 2
    x = startRefx   
    y += yIncrement * 2


#Display the image
cv.imshow("Display", cubeBottomRight)
cv.waitKey(0)
cv.destroyAllWindows()