import cv2 as cv
import time
import imutils
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter
import pandas as pd
import math

image = "copyTop.png"
#process the image to be looked at
imageTop = cv.imread(image)
imageTop = imutils.rotate(imageTop, 180)

#colors as BGR
white = (255, 255 ,255)
red = (0, 0, 255)
green = (0, 255, 0)
yellow = (0, 255, 255)
orange = (80, 150, 255)
blue = (200, 118, 55)


lineSize = 1

x = 220
y = 30

xL = x + 270
yL = y + 270
imageTop = cv.rectangle(imageTop, (x, y) , (xL, yL), orange, lineSize)

listOrange = [
    (250, 165),
    (210, 150),
    (160 ,120),
    (250, 220),
    (210, 195),
    (170, 165),
    (320, 270),
    (290, 240),
    (260, 227)
]

listWhite = [
    (465, 120)
]



#returns dominant colour of image as BGR value
def get_dominant_color(image, k=4, image_processing_size = None):
    if image_processing_size is not None:
        image = cv.resize(image, image_processing_size, 
                            interpolation = cv.INTER_AREA)
    image = image.reshape((image.shape[0] * image.shape[1], 3)) 
    clt = KMeans(n_clusters = k)
    labels = clt.fit_predict(image)
    label_counts = Counter(labels)
    dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]
    return list(dominant_color)

#returns list of colours based on input list of positions
def getColours(list, image, face):
    print("Scanning: " + face)
    for i in range(len(list)):
        XY = list[i]
        x = XY[0]
        y = XY[1]
        P1 = (x, y)
        squareSize = 12
        P2 = (x + squareSize, y + squareSize)
        
        image = cv.rectangle(image, P1, P2, blue, lineSize)
        image = cv.putText(image, str(i), P2, 1, 1, blue)
        
        section = image[int(P1[1]):int(P2[1]), int(P1[0]) : int(P2[0])]
        #section = cv.cvtColor(section, cv.COLOR_RGB2HSV)
        section = cv.resize(section, (200,200))
        color = get_dominant_color(section)
        #color.reverse() #BGR to RGB
        color = [round(i) for i in color]
        print(color)

getColours(listOrange, imageTop, "Orange")
getColours(listWhite, imageTop, "White")
#show result
cv.imshow("Window", imageTop)
cv.waitKey(0)
cv.destroyAllWindows()