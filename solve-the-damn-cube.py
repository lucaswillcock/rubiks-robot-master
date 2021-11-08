import time
import logging

try:
    import RPi.GPIO as GPIO
    from kociemba import *
except ModuleNotFoundError:
    logging.error("Module not found.")    

#class that establishs a motor, has half turn and quarter
class encodedStepper:
    #iniates motor oject assigning pins
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