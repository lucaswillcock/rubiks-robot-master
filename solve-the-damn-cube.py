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
        
def takePhotos():
        cameraTop = cv.VideoCapture(0)
        _, topImg = cameraTop.read()
        topImg = cv.flip(topImg, 1)
        cv.imwrite("top.png", topImg)
        print("Image capture successful")
        LCD.lcd_display_string("image 1 successful")
        
        cameraBottom = cv.VideoCapture(1)
        _, botImg = cameraTop.read()
        topImg = cv.flip(botImg, 1)
        cv.imwrite("bottom.png", botImg)
        print("Image capture successful")
        LCD.lcd_display_string("image2 successful")
        
takePhotos()