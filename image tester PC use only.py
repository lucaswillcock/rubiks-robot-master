import cv2 as cv
import imutils

imageTop = cv.imread("copyTop.png")
imageBottom = cv.imread("copyBottom.png")

#imageTop = imutils.rotate(imageTop, 180)

lineSize = 1

blue = (255, 100, 100)

listBack = [
    (190 ,150), #1
    (225, 175), #2
    (280, 210), #3
    (195, 205), #4
    (240, 235), #5
    (290, 280), #6
    (225, 290), #7
    (250, 300), #8
    (290, 330)  #9
]

listLeft = [
    (350 ,220), #1
    (400, 180), #2
    (450, 155), #3
    (350, 270), #4
    (400, 240), #5
    (445, 205), #6
    (345, 330), #7
    (395, 295), #8
    (420, 290)  #9
]

listUp = [
    (330 ,170), #1
    (260, 135), #2
    (205, 115), #3
    (370, 135), #4
    (325, 110), #5
    (270, 95), #6
    (410, 110), #7
    (370, 95), #8
    (293, 78)  #9
]

listDown = [
    (210 ,290), #1
    (260, 270), #2
    (320, 240), #3
    (260, 310), #4
    (310, 290), #5
    (370, 260), #6
    (338, 332), #7
    (360, 315), #8
    (400, 290)  #9
]

listRight = [
    (330, 80), #1
    (380, 120), #2
    (425, 175), #3
    (330, 120), #4
    (375, 150), #5
    (425, 200), #6
    (330, 180), #7
    (390, 220), #8
    (430, 245)  #9
]

listFront = [
    (198, 174), #1
    (250, 120), #2
    (295, 80), #3
    (200, 200), #4
    (240, 160), #5
    (290, 130), #6
    (190, 250), #7
    (230, 230), #8
    (280, 190)  #9
]

#returns list of colours based on input list of positions
def getColours(list, image, face):
    #this loops takes small snippet of colour and gets BGR value for the dominant colour
    #Then returns cubie value
    for i in range(len(list)):
        XY = list[i]
        x = XY[0]
        y = XY[1]
        P1 = (x, y)
        squareSize = 10
        P2 = (x + squareSize, y + squareSize)
        
        image = cv.rectangle(image, P1, P2, blue, lineSize)
        image = cv.putText(image, face + str(i+1), P2, 1, 1, blue)
    

getColours(listBack, imageTop, "B")
getColours(listLeft, imageTop, "L")
getColours(listUp, imageTop, "U")

getColours(listRight, imageBottom, "R")
getColours(listFront, imageBottom, "F")
getColours(listDown, imageBottom, "D")

#show result
cv.imshow("Window", imageTop)
cv.imshow("window2", imageBottom)
cv.waitKey(0)
cv.destroyAllWindows()