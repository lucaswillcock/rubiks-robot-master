import cv2 as cv

imageTop = "copyTop.png"
imageBottom = "copyBottom.png"

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
    (302, 40)  #9
]

listDown = [
    (210 ,390), #1
    (250, 370), #2
    (289, 340), #3
    (250, 410), #4
    (300, 395), #5
    (350, 370), #6
    (325, 430), #7
    (350, 415), #8
    (390, 395)  #9
]

listRight = [
    (315 ,195), #1
    (360, 230), #2
    (415, 277), #3
    (320, 245), #4
    (375, 280), #5
    (415, 310), #6
    (320, 300), #7
    (370, 330), #8
    (415, 355)  #9
]

listFront = [
    (225, 245), #1
    (245, 235), #2
    (285, 205), #3
    (200, 300), #4
    (225, 285), #5
    (280, 240), #6
    (195, 350), #7
    (230, 330), #8
    (280, 300)  #9
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
        squareSize = 12
        P2 = (x + squareSize, y + squareSize)
        
        image = cv.rectangle(image, P1, P2, blue, lineSize)
        image = cv.putText(image, str(i+1), P2, 1, 1, blue)
    

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