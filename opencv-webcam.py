import cv2 as cv
import numpy as np

#image parameters
startRefX = 200
startRefY = 200

#process image
cubeBottomRight = cv.imread("cube.jpeg")
cubeBottomRight = cv.circle(cubeBottomRight, (startRefX, startRefY), 50, (255, 255, 255), 10)

#Display the image
cv.imshow("Display", cubeBottomRight)
cv.waitKey(0)
cv.destroyAllWindows()