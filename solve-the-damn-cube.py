#
import time
from pyfirmata import *
import cv2 as cv
from pyfirmata import Arduino
from kociemba import *
from PIL import *
import I2C_LCD_driver as lcdLib
#import motor
    
#timing
pulseWidth = 0.01
enableWait = 0.005

#Arduino Pin Assignments
pulsePin = 10
directionPin = 10
motorUpEnable = 10
motorDownEnable = 10
motorFrontEnable = 10
motorBackEnable = 10
motorRightEnable = 10
motorLeftEnable = 10
buttonControl = 10

#create motors

#define LCD
LCD = lcdLib.lcd()

#Umotor = motor(motorUpEnable, pulsePin, directionPin)
        
class cameraObject:
    def __init__(self, port) -> None:
        self.camera = cv.VideoCapture(port)

    def getImage(self):
        _, image = self.camera.read()
        image = cv.flip(image, 1)
        cv.imwrite("Image.jpg", image)
        print("Image capture successful")
        LCD.lcd_display_string("image successful")
        
topCam = cameraObject(0)
bottomCam = cameraObject(1)

topCam.getImage()
bottomCam.getImage()