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
LCD.lcd_display_string("Hello muthfuckas")
#Umotor = motor(motorUpEnable, pulsePin, directionPin)
        
def takePhoto(port, imageName):
        camera0 = cv.VideoCapture(port)
        _, image = camera0.read()
        #topImg = cv.flip(topImg, 1)
        cv.imwrite(imageName, image)
        print("Image capture successful")
        LCD.lcd_display_string("image successful")
        camera0.release()
        
takePhoto(0, "top.png")
LCD.lcd_clear()
LCD.lcd_display_string("move")
#takePhoto(-1, "bottom.png")