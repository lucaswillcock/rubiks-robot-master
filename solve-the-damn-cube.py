#
import time
import logging
from pyfirmata import *
import cv2 as cv
from pyfirmata import Arduino
from kociemba import *
from PIL import *

try:
    import RPi.GPIO as GPIO
    from kociemba import *
except ModuleNotFoundError as error:
    logging.error(error)
    
logging.basicConfig(level = logging.CRITICAL)
    
try:
    arduino = Arduino("/dev/tty.usbserial-142140")
    logging.info("Arduino connected successfully")
except serial.serialutil.SerialException as e:
    logging.error(" Couldnt find board")
    logging.error(e)

#Arduino Pin Assignments
pulsePin = 10
directionPin = 10
motorUpEnable = 10
motorDownEnable = 10
motorFrontEnable = 10
motorBackEnable = 10
motorRightEnable = 10
motorLeftEnable = 10

#Raspberry Pi Pin Assignments
buttonLeft = 10
buttonRight = 10

#class that establishs a motor, has half turn and quarter
class encodedStepper:
    #iniates motor object assigning pins
    def __init__(self, position, enable, pulse, direction, speed, stepRatio):
        self.enable = enable
        self.pulse = pulse
        self.direction = direction
        self.speed = speed
        self.location = position
        self.pulsesFullTurn = 360*(1.8*stepRatio)
        
        #disables motor, allows it to turn freely
        arduino.digital[self.enable].write(1)
        
    def rotateQuarter(self, direction):
        arduino.digital[self.enable].write(0)
        arduino.digital[self.direction].write(direction)
        
        for i in range(self.pulsesFullTurn/4):
            arduino.digital[self.pulse].write(1)
            time.sleep(self.speed)
            arduino.digital[self.pulse].write(1)
            time.sleep(self.speed)
        arduino.digital[self.enable].write(0)
        
    def rotateHalf(self, direction):
        arduino.digital[self.enable].write(0)
        arduino.digital[self.direction].write(direction)
        
        for i in range(self.pulsesFullTurn/2):
            arduino.digital[self.pulse].write(1)
            time.sleep(self.speed)
            arduino.digital[self.pulse].write(1)
            time.sleep(self.speed)
        arduino.digital[self.enable].write(0)
        
class cameraObject:
    def __init__(self, port) -> None:
        self.camera = cv.VideoCapture(port)

    def getImage(self):
        _, image = self.camera.read()
        image = cv.flip(image, 1)
        cv.putText(image, "Big Fat Cock", (100, 100), cv.FONT_HERSHEY_COMPLEX, 5, (255, 255, 255))
        cv.imwrite("Image.jpg", image)
        print("Image capture successful")
        
webcam = cameraObject(0)
webcam.getImage()