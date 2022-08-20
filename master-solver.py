import cv2 as cv
import ledssss as ledssss
from sklearn.cluster import KMeans
from collections import Counter
from webcolors import *
from scipy.spatial import KDTree
import kociemba
import RPi.GPIO as GPIO
import time
import I2C_LCD_driver as LCD
import random

GPIO.setmode(GPIO.BCM)

#Set brightness and colour for taking photos
brightness = 50
whiteLight = (brightness, brightness - 2, brightness - 4)

#size of lines in graphics, used for debugging visually
lineSize = 1

#Define led rings by order in chain
ringBack = ledssss.ledRing(1)
ringUp = ledssss.ledRing(2)
ringLeft = ledssss.ledRing(3)
ringDown = ledssss.ledRing(4)
ringRight = ledssss.ledRing(5)
ringFront = ledssss.ledRing(6)

lcd = LCD.lcd()

pulseDelay = 0.0002 #0.0002

pulse = 27
directionPin = 17

Rmotor = 22
Bmotor = 5
Umotor = 6
Lmotor = 13
Dmotor = 19
Fmotor = 26

#Button set up
buttonPin = 21
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

CW = 0
CCW = 1

#400 turns per revolution with DM542 drivers
quarterTurn = 100
halfTurn = 200

#colors as RGB
white = (255, 255 ,255)
red = (255, 127, 95)
green = (147, 255, 203)
black = (100, 100, 100)
orange = (255, 200, 120)
blue = (55, 190, 255)
blue2 = (186, 253, 255)
orange2 = (255, 132, 63)
green2 = (76, 255, 222)
green3 = (198, 255, 245)
green4 = (98, 253, 172)

rgb_list = [
    white, 
    red, 
    green, 
    black, 
    orange, 
    blue, 
    blue2,
    orange2,
    green2,
    green3,
    green4
    ]

#List should match above list of colours but with letter associated to that colours side
names_list = [
    "U",
    "R",
    "F",
    "D",
    "L",
    "B",
    "B",
    "L",
    "F",
    "F",
    "F"
    ]

#Each of these lists defines XY positions of individual cubies for that respective side
listBack = [(190 ,150), (225, 175), (280, 210), (195, 205), (240, 235), (290, 280), (225, 290), (250, 300), (290, 330)]
listLeft = [(350 ,220), (400, 180), (450, 155), (350, 270), (400, 240), (445, 205), (345, 330), (395, 295), (420, 290)]
listUp = [(330 ,170), (260, 135), (205, 115), (370, 135), (325, 110), (270, 95), (410, 110), (370, 95), (293, 78)]
listDown = [(210 ,290), (260, 270), (320, 240), (260, 310), (310, 290), (370, 260), (338, 332), (360, 315), (400, 290)]
listRight = [(330, 80), (380, 120), (425, 175), (330, 120), (375, 150), (425, 200), (330, 180), (390, 220), (430, 245)]
listFront = [(198, 174), (250, 120), (295, 80), (200, 200), (240, 160), (290, 130), (190, 250), (230, 230), (280, 190)]

def displayTopLine(text):
    lcd.lcd_display_string("                ", 1)
    lcd.lcd_display_string(text, 1)
    print(text)
    
def displayBottomLine(text):
    lcd.lcd_display_string("                ", 2)
    lcd.lcd_display_string(text, 2)
    print(text)

#class defines motor object
class motor:
    def __init__(self, enable, pulse, direction, delay):
        self.en = enable
        self.pulse = pulse
        self.dir = direction
        self.dly = delay
        
        GPIO.setup(enable, GPIO.OUT)
        GPIO.setup(pulse, GPIO.OUT)
        GPIO.setup(direction, GPIO.OUT)
        
        GPIO.output(self.en, 0)
        
    def rotate(self, direction, distance):
        GPIO.output(self.en, 1)
        GPIO.output(self.dir, direction)
        for i in range(distance - 5): #-5
            GPIO.output(self.pulse, 1)
            time.sleep(self.dly)
            GPIO.output(self.pulse, 0)
            time.sleep(self.dly)
            
        print(direction)
        
        #time.sleep(0.05)
        if direction == 0:
            GPIO.output(self.dir, 1)
            GPIO.output(self.pulse, 1)
            time.sleep(self.dly)
            GPIO.output(self.pulse, 0)
            time.sleep(self.dly)
        elif direction == 1:
            GPIO.output(self.dir, 0)
            GPIO.output(self.pulse, 1)
            time.sleep(self.dly)
            GPIO.output(self.pulse, 0)
            time.sleep(self.dly)
        
        print(direction)
        
        GPIO.output(self.en, 0)

#executes given string of moves, note motor left is switched as a software fix
def executeMoves(solution):
    
    displayBottomLine("")
    displayTopLine("3..")
    lightsAll((50, 10, 0))
    lightsAll((0, 0, 0))
    time.sleep(0.2)
    displayTopLine("3.. 2..")
    lightsAll((50, 10, 0))
    lightsAll((0, 0, 0))
    time.sleep(0.2)
    displayTopLine("3.. 2.. 1..")
    lightsAll((50, 10, 0))
    lightsAll((0, 0, 0))
    time.sleep(0.2)
    lightsAll((0, 40, 0))
    displayTopLine("3.. 2.. 1.. Go!")
    
    
    solutionList = solution.split()
    start = time.time()
    for i in range(len(solutionList)):
        print(solutionList[i])
        if solutionList[i] == "U":
            UMotor.rotate(CW, quarterTurn)
        
        elif solutionList[i] == "U'":
            UMotor.rotate(CCW, quarterTurn)
            
        elif solutionList[i] == "U2":
            UMotor.rotate(CCW, halfTurn)
            
        elif solutionList[i] == "L":
            LMotor.rotate(CCW, quarterTurn)
        
        elif solutionList[i] == "L'":
            LMotor.rotate(CW, quarterTurn)
            
        elif solutionList[i] == "L2":
            LMotor.rotate(CCW, halfTurn)
            
        elif solutionList[i] == "R":
            RMotor.rotate(CW, quarterTurn)
        
        elif solutionList[i] == "R'":
            RMotor.rotate(CCW, quarterTurn)
            
        elif solutionList[i] == "R2":
            RMotor.rotate(CCW, halfTurn)
            
        elif solutionList[i] == "D":
            DMotor.rotate(CW, quarterTurn)
        
        elif solutionList[i] == "D'":
            DMotor.rotate(CCW, quarterTurn)
            
        elif solutionList[i] == "D2":
            DMotor.rotate(CCW, halfTurn)
            
        elif solutionList[i] == "F":
            FMotor.rotate(CW, quarterTurn)
        
        elif solutionList[i] == "F'":
            FMotor.rotate(CCW, quarterTurn)
            
        elif solutionList[i] == "F2":
            FMotor.rotate(CCW, halfTurn)
            
        elif solutionList[i] == "B":
            BMotor.rotate(CW, quarterTurn)
        
        elif solutionList[i] == "B'":
            BMotor.rotate(CCW, quarterTurn)
            
        elif solutionList[i] == "B2":
            BMotor.rotate(CCW, halfTurn)
            
    end = time.time()
    displayTopLine("Time: " + str(round(end - start, 3)) + "s")
    ringBack.on((0, 0, 60))
    ringUp.on((20, 20, 20))
    ringLeft.on((50, 10, 0))
    ringDown.on((30, 30, 0))
    ringRight.on((60, 0, 0))
    ringFront.on((0, 60, 0))

#Turns all lights off, takes no argument
def lightsAll(color):
    ringRight.on(color)
    ringDown.on(color)
    ringFront.on(color)
    ringBack.on(color)
    ringUp.on(color)
    ringLeft.on(color)

#takes photo from given port, saves and returns image
def takePhoto(port, imageName):
        camera0 = cv.VideoCapture(port)
        _, image = camera0.read()
        cv.imwrite(imageName, image)
        displayTopLine("Image capture successful")
        return image
        camera0.release()
        
#takes photo from top camera with backlighting
def photoTop():
    ringBack.on(whiteLight)
    ringUp.on(whiteLight)
    ringLeft.on(whiteLight)
    ringRight.off()
    ringDown.off()
    ringFront.off()
    time.sleep(0.2)
    image = takePhoto(2, "top.png")
    return image

#takes photo from bottom camera with backlighting  
def photoBottom():
    ringRight.on(whiteLight)
    ringDown.on(whiteLight)
    ringFront.on(whiteLight)
    ringBack.off()
    ringUp.off()
    ringLeft.off()
    time.sleep(0.2)
    image = takePhoto(0, "bottom.png")
    return image

#get colour as string from RGB
def convert(rgb):
    
    kdt_db = KDTree(rgb_list)
    distance, index = kdt_db.query(rgb)
    return  names_list[index]

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
    lightsAll((random.randint(0, 50), random.randint(0, 50), random.randint(0, 50)))
    faceListasLetters = []
    faceListasRGBvalues = []
    
    #this loops takes small snippet of colour and gets BGR value for the dominant colour
    #Then returns cubie value
    for i in range(len(list)):
        XY = list[i]
        x = XY[0]
        y = XY[1]
        P1 = (x, y)
        squareSize = 10
        P2 = (x + squareSize, y + squareSize)
        
        #image = cv.rectangle(image, P1, P2, orange, lineSize)
        #image = cv.putText(image, str(i+1), P2, 1, 1, orange)
        
        section = image[int(P1[1]):int(P2[1]), int(P1[0]) : int(P2[0])]
        section = cv.resize(section, (200,200))
        color = get_dominant_color(section)
        color = [round(i) for i in color]
        color.reverse()
        color_name = convert(color)
        displayTopLine("Scanning: " + face + str(i+1) + " = " + color_name)
        displayBottomLine(str(color))
        faceListasRGBvalues.append(color)
        faceListasLetters.append(color_name)
    
    cv.imwrite(face + ".png", image)
    faceListasLetters[4] = face
    print(face + ": " + str(faceListasLetters))
    return faceListasLetters, faceListasRGBvalues

#Create and define motor objects
RMotor = motor(Rmotor, pulse, directionPin, pulseDelay)
BMotor = motor(Bmotor, pulse, directionPin, pulseDelay)
UMotor = motor(Umotor, pulse, directionPin, pulseDelay)
LMotor = motor(Lmotor, pulse, directionPin, pulseDelay)
DMotor = motor(Dmotor, pulse, directionPin, pulseDelay)
FMotor = motor(Fmotor, pulse, directionPin, pulseDelay)

def homeScreen():
    ringBack.on((0, 0, 60))
    ringUp.on((20, 20, 20))
    ringLeft.on((50, 10, 0))
    ringDown.on((30, 30, 0))
    ringRight.on((60, 0, 0))
    ringFront.on((0, 60, 0))
    displayTopLine("#Machine Ready#")
    displayBottomLine("Press to solve...")
    
homeScreen()
    
while 1:
    if GPIO.input(buttonPin) == GPIO.HIGH:
        
        try:
            #Take photos
            imageTop = photoTop()
            imageBottom = photoBottom()

            #lighyts off
            lightsAll((0, 0, 0))

            #get lists of faces
            backLetters, backRGB = getColours(listBack, imageTop, "B")
            leftLetters, leftRGB = getColours(listLeft, imageTop, "L")
            upLetters, upRGB= getColours(listUp, imageTop, "U")

            rightLetters, rightRGB = getColours(listRight, imageBottom, "R")
            frontLetters, frontRGB = getColours(listFront, imageBottom, "F")
            downLetters, downRGB = getColours(listDown, imageBottom, "D")

            #combine lists in  correct order for solving
            totalListRGB =[]
            totalListLetters = []
            totalListRGB = upRGB + rightRGB + frontRGB + downRGB + leftRGB + backRGB
            totalListLetters = upLetters + rightLetters + frontLetters + downLetters + leftLetters + backLetters


            lcd.lcd_clear()

            Utotal = totalListLetters.count("U")
            Rtotal = totalListLetters.count("R")
            Ftotal = totalListLetters.count("F")
            Dtotal = totalListLetters.count("D")
            Ltotal = totalListLetters.count("L")
            Btotal = totalListLetters.count("B")
            
            totals = [Utotal, Rtotal, Ftotal, Dtotal, Ltotal, Btotal]

            displayTopLine("W:" + str(Utotal) + " R:" + str(Rtotal) + " G:" + str(Ftotal))
            displayBottomLine("B:" + str(Dtotal) + " O:" + str(Ltotal) + " B:" + str(Btotal))

            cube = ""
            for i in range(len(totalListLetters)):
                cube = cube + totalListLetters[i]

            solution = kociemba.solve(cube)
            print(solution)

            executeMoves(solution)
            
            time.sleep(10)
            
            homeScreen()
            
        except ValueError:
            lightsAll((60, 0, 0))
            for item in totals:
                if item != 9:
                    displayTopLine("Error")
                    displayBottomLine("Couldn't read cube")
                else:
                    displayTopLine("Error")
                    displayBottomLine("Can't find solution")
                    
            time.sleep(10)
            
            homeScreen()
        
        except:
            lightsAll((60, 0, 0))
            displayTopLine("ya fucked it")
            displayBottomLine("reboot machine")
            
            time.sleep(10)
            
            homeScreen()