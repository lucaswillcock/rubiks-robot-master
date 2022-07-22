import cv2 as cv
import numpy as np
import imutils

#image parameters
dotsize =  4
dotthickness = 4
colour = (255, 255, 255)

startRefx = 517
startRefy = 45
startRef = (startRefx, startRefy)



xIncrement = 207
yIncrement = 64

#process image
cubeBottomRight = cv.imread("cube.png")
#cubeBottomRight = imutils.rotate(cubeBottomRight, -0.4)
x = startRefx
y = startRefy
for i in range(7):
    cubeBottomRight = cv.circle(cubeBottomRight, (x, y), dotsize, colour, dotthickness)
    y += yIncrement
    if i >= 3:
        yIncrement = 75
    else:
        yIncrement += 15

#Display the image
cv.imshow("Display", cubeBottomRight)
cv.waitKey(0)
cv.destroyAllWindows()