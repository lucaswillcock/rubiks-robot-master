from turtle import pos
import cv2 as cv
import time
import imutils
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter
import pandas as pd 

image = "topCopy.png"

imageTop = cv.imread(image)
imageTop = imutils.rotate(imageTop, 180)
#imageTop = cv.cvtColor(imageTop, cv.COLOR_BGR2HSV)

blue = (255, 0, 0)
lineSize = 2

x = 220
y = 30

xL = x + 270
yL = y + 270
imageTop = cv.rectangle(imageTop, (x, y) , (xL, yL), blue, lineSize)

posList = [
    (235 ,110), 
    (280, 140),
    (320, 165),
    (235, 165)
]

index=["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

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

for i in range(len(posList)):
    XY = posList[i]
    x = XY[0]
    y = XY[1]
    P1 = (x, y)
    squareSize = 20
    P2 = (x + squareSize, y + squareSize)
    
    #imageTop = cv.rectangle(imageTop, P1, P2, blue, lineSize)
    
    section = imageTop[int(P1[1]):int(P2[1]), int(P1[0]) : int(P2[0])]
    #section = cv.cvtColor(section, cv.COLOR_RGB2HSV)
    section = cv.resize(section, (200,200))
    
    color = get_dominant_color(section)
    
    color.reverse()
    print(color)
    colourString = recognize_color(color[0], color[1], color[2])
    print(colourString  )
 
# imageTop = imageTop[10:100, 50:110]


#show result
cv.imshow("Window", imageTop)
cv.imshow("Window 2", section)
cv.waitKey(0)
cv.destroyAllWindows()