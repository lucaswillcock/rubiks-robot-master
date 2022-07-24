import RPi.GPIO as GPIO
import time
import I2C_LCD_driver as LCD

GPIO.setmode(GPIO.BCM)

lcd = LCD.lcd()

pulseDelay = 0.0002

pulse = 27
directionPin = 17

Rmotor = 22
Bmotor = 5
Umotor = 6
Lmotor = 13
Dmotor = 19
Fmotor = 26

CW = 0
CCW = 1

quarterTurn = 100
halfTurn = 200

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
        for i in range(distance):
            GPIO.output(self.pulse, 1)
            time.sleep(self.dly)
            GPIO.output(self.pulse, 0)
            time.sleep(self.dly)
        
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
        GPIO.output(self.en, 0)
        
RMotor = motor(Rmotor, pulse, directionPin, pulseDelay)
BMotor = motor(Bmotor, pulse, directionPin, pulseDelay)
UMotor = motor(Umotor, pulse, directionPin, pulseDelay)
LMotor = motor(Lmotor, pulse, directionPin, pulseDelay)
DMotor = motor(Dmotor, pulse, directionPin, pulseDelay)
FMotor = motor(Fmotor, pulse, directionPin, pulseDelay)

def executeMoves(solution):
    solutionList = solution.split()
    start = time.time()
    for i in range(len(solutionList)):
        if solutionList[i] == "U":
            UMotor.rotate(CW, quarterTurn)
        
        elif solutionList[i] == "U'":
            UMotor.rotate(CCW, quarterTurn)
            
        elif solutionList[i] == "U2":
            UMotor.rotate(CCW, halfTurn)
            
        elif solutionList[i] == "L":
            LMotor.rotate(CW, quarterTurn)
        
        elif solutionList[i] == "L'":
            LMotor.rotate(CCW, quarterTurn)
            
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
    print("Finished in: " + str(round(end - start, 3)))
            
            
executeMoves("B2 R2 L D L' U' F2 D2 R D R2 U F2 R2 U2 B2 D' F2 D2")