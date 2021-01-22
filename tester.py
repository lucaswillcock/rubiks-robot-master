from tkinter import *

import json
import time

import RPi.GPIO as GPIO

from imports import init

init.installLibraries()

#import variable from JSON file
with open("rubiks-data.json", "r") as data:
    readData = data.read()

jsonData = json.loads(readData)
windowWidth = jsonData["width"]
windowHeight = jsonData["height"]
buttonHeight = jsonData["buttonHeight"]
buttonWidth = jsonData["buttonWidth"]
padding = jsonData["padding"]
currentCube = list(jsonData["solvedCubeNotationList"])
cubeColoursList = jsonData["cubeColoursList"]
buttonIDList = jsonData["buttonIDList"]

UMotorEN = jsonData["motorUEN"]
FMotorEN = jsonData["motorFEN"]
DMotorEN = jsonData["motorDEN"]
BMotorEN = jsonData["motorBEN"]
LMotorEN = jsonData["motorLEN"]
RMotorEN = jsonData["motorREN"]

delay = jsonData["delay"]

quarterTurn = jsonData["quarterTurn"]
halfTurn = jsonData["halfTurn"]

CC = jsonData["CC"]
CCW = jsonData["CCW"]

direction = jsonData["direction"]
clock = jsonData["clock"]

data.close()

print("JSON load complete")

#class for motor control
class motor:
    def __init__(self, enable, clock, direction, delay):
        self.en = enable
        self.clk = clock
        self.dir = direction
        self.dly = delay
        
        GPIO.output(self.en, "high")
        
    def rotate(self, direction, distance):
        GPIO.output(self.dir, direction)
        GPIO.output(self.en, "low")
        for i in range(distance):
            GPIO.output(self.clk, "high")
            time.sleep(self.dly)
            GPIO.output(self.clk, "low")
            time.sleep(self.dly)
            
        GPIO.output(self.en, "high")

UMotor = motor(UMotorEN, clock, direction, delay)
FMotor = motor(FMotorEN, clock, direction, delay)
DMotor = motor(DMotorEN, clock, direction, delay)
BMotor = motor(BMotorEN, clock, direction, delay)
LMotor = motor(LMotorEN, clock, direction, delay)
RMotor = motor(RMotorEN, clock, direction, delay)

print("motors initiated")

root = Tk()
root.title("Motor tester")
#root.config(bg = "light grey")
root.minsize(windowWidth, windowHeight)

motor1button = Button(root, text = "motor 1")
motor1button.grid(column = 0, row = 0)




root.mainloop()