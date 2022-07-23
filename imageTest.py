import cv2 as cv
import time
import imutils
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter
import pandas as pd
import math

imageTop = "copyTop.png"
imageBottom = "copyBottom.png"

#process the image to be looked at
imageBottom = cv.imread(imageBottom)
imageTop = cv.imread(imageTop)
imageTop = imutils.rotate(imageTop, 180)

#colors as BGR
white = (255, 255 ,255)
red = (0, 0, 255)
green = (0, 255, 0)
yellow = (0, 255, 255)
orange = (80, 150, 255)
blue = (200, 118, 55)

lineSize = 1

listBack = [
    (160 ,120), #1
    (205, 145), #2
    (250, 165), #3
    (170, 165), #4
    (210, 195), #5
    (250, 220), #6
    (170, 190), #7
    (220, 240), #8
    (260, 270)  #9
]

listLeft = [
    (300 ,165), #1
    (350, 140), #2
    (390, 115), #3
    (305, 220), #4
    (345, 195), #5
    (390, 160), #6
    (310, 265), #7
    (347, 235), #8
    (390, 185)  #9
]

listUp = [
    (275 ,130), #1
    (220, 105), #2
    (185, 85), #3
    (320, 95), #4
    (275, 75), #5
    (220, 60), #6
    (370, 75), #7
    (320, 55), #8
    (302 , 40)  #9
]

listDown = [
    (210 ,390), #1
    (250, 370), #2
    (289, 340), #3
    (320, 95), #4
    (275, 75), #5
    (220, 60), #6
    (370, 75), #7
    (320, 55), #8
    (302 , 40)  #9
]

listRight = [
    (275 ,130), #1
    (220, 105), #2
    (185, 85), #3
    (320, 95), #4
    (275, 75), #5
    (220, 60), #6
    (370, 75), #7
    (320, 55), #8
    (302 , 40)  #9
]

listFront = [
    (275 ,130), #1
    (220, 105), #2
    (185, 85), #3
    (320, 95), #4
    (275, 75), #5
    (220, 60), #6
    (370, 75), #7
    (320, 55), #8
    (302 , 40)  #9
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
    #this loops takes small snippet of colour and gets BGR value for the dominant colour
    #Then returns cubie value
    for i in range(len(list)):
        XY = list[i]
        x = XY[0]
        y = XY[1]
        P1 = (x, y)
        squareSize = 12
        P2 = (x + squareSize, y + squareSize)
        
        image = cv.rectangle(image, P1, P2, blue, lineSize)
        image = cv.putText(image, str(i+1), P2, 1, 1, blue)
        
        section = image[int(P1[1]):int(P2[1]), int(P1[0]) : int(P2[0])]
        section = cv.resize(section, (200,200))
        color = get_dominant_color(section)
        color = [round(i) for i in color]
        print(str(color) + str(i+1))

getColours(listBack, imageTop, "Blue")
getColours(listLeft, imageTop, "Orange")
getColours(listUp, imageTop, "White")

getColours(listRight, imageBottom, "Blue")
getColours(listFront, imageBottom, "Orange")
getColours(listDown, imageBottom, "White")

#show result
cv.imshow("Window", imageTop)
cv.imshow("window2", imageBottom)
cv.waitKey(0)
cv.destroyAllWindows()