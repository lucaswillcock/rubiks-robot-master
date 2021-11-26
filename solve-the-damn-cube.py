import time
import logging
from pyfirmata import *
import cv2 as cv
from pyfirmata import Arduino

try:
    #import RPi.GPIO as GPIO
    from kociemba import *
except ModuleNotFoundError as error:
    logging.error(error)
    
logging.basicConfig(level = logging.CRITICAL)
    
try:
    arduino = Arduino("/dev/tty.usbserial-142140")
    logging.info("Arduino connected successfully")
except serial.serialutil.SerialException as e:
    logging.error(" Couldnt find board")

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
        
        GPIO.setup(enable, GPIO.OUT)
        GPIO.setup(pulse, GPIO.OUT)
        GPIO.setup(direction, GPIO.OUT)
        
        logging.info("")
        
        #disables motor, allows it to turn freely
        GPIO.output(self.enable, 1)
        
    def rotateQuarter(self, direction):
        GPIO.output(self.enable, 0)
        GPIO.output(self.direction, direction)
        for i in range(self.pulsesFullTurn/4):
            GPIO.output(self.pulse, 1)
            time.sleep(self.speed)
            GPIO.output(self.pulse, 0)
            time.sleep(self.speed)
        GPIO.output(self.en, 1)
            
    def rotateHalf(self, direction):
        GPIO.output(self.enable, 0)
        GPIO.output(self.direction, direction)
        for i in range(self.pulsesFullTurn/4):
            GPIO.output(self.pulse, 1)
            time.sleep(self.speed)
            GPIO.output(self.pulse, 0)
            time.sleep(self.speed)            
        GPIO.output(self.en, 1)