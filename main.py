from tkinter import *
from tkinter import Text
import kociemba as k
import json
import time

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
microstep = jsonData["microstep"]

data.close()

#sets the colour of cube button
def setBColor(self, color):
    self.config(bg = color, activebackground = color, highlightbackground = color)
    
def listToString(listx):
    xyz = ""
    for item in range(len(listx)):
        xyz =  xyz + listx[item]
    return xyz

#establish root environment, name and bounds
root = Tk()
root.title("Rubik's Robot")
root.config(bg = "light grey")
root.minsize(windowWidth, windowHeight)
root.maxsize(windowWidth, windowHeight)

text = Text(root, width = 45, height = 30)
text.grid(column = 1, row = 0, columnspan = 2, pady = 5, padx = 5)

cubeInputFrame = LabelFrame(root, text = "Cube Interface", padx = 3, pady = 5, bg = "light grey")
cubeInputFrame.grid(row = 0, column = 0, padx = 4, pady = 8, rowspan = 2)

def outputText(output):
    text.insert(END, "\n" + output + "\n")
    text.yview_pickplace("end")

#placeholder for the rpigpio library
def GPIO_output(a, b):
    outputText("pin " + str(a) + " set to " + str(b))

#class for motor control
class motor:
    def __init__(self, enable, clock, direction, delay):
        self.en = enable
        self.clk = clock
        self.dir = direction
        self.dly = delay
        
        GPIO_output(self.en, "high")
        
    def rotate(self, direction, distance):
        GPIO_output(self.en, "low")
        GPIO_output(self.dir, direction)
        for i in range(distance):
            GPIO_output(self.clk, "high")
            time.sleep(self.dly)
            GPIO_output(self.clk, "low")
            time.sleep(self.dly)
            
        GPIO_output(self.en, "high")

UMotor = motor(UMotorEN, clock, direction, delay)
FMotor = motor(FMotorEN, clock, direction, delay)
DMotor = motor(DMotorEN, clock, direction, delay)
BMotor = motor(BMotorEN, clock, direction, delay)
LMotor = motor(LMotorEN, clock, direction, delay)
RMotor = motor(RMotorEN, clock, direction, delay)

#change colour of a button
def changeColour(self, buttonName):
    currentColour = cubeColoursList.index(self.cget("bg"))
    if (currentColour + 1) == len(cubeColoursList):
        setBColor(self, cubeColoursList[0])
    else:
        currentColour = currentColour + 1
        setBColor(self, cubeColoursList[currentColour])
        
    colour = self.cget("bg")
    
    if colour == "white":
        currentCube[buttonIDList.index(buttonName)] = "U"
        #self.config(text = "U")
    elif colour == "blue":
        currentCube[buttonIDList.index(buttonName)] = "L"
        #self.config(text = "L")
    elif colour == "orange":
        currentCube[buttonIDList.index(buttonName)] = "F"
        #self.config(text = "F")
    elif colour == "yellow":
        currentCube[buttonIDList.index(buttonName)] = "D"
        #self.config(text = "D")
    elif colour == "green":
        currentCube[buttonIDList.index(buttonName)] = "R"
        #self.config(text = "R")
    elif colour == "red":
        currentCube[buttonIDList.index(buttonName)] = "B"
        #self.config(text = "B")
        
    outputText("list update: " + listToString(currentCube))
    
    return currentCube

#draw one square
def createOneSquare(columnNumber, rowNum, colourValue, listValue):
    buttonObject = buttonIDList[listValue]
    buttonName = buttonObject
    listValue += 1
    buttonObject = Button(cubeInputFrame, padx = buttonWidth, pady = buttonHeight)
    #buttonObject.config(text = buttonName)
    buttonObject.config(command = lambda: changeColour(buttonObject, buttonName))
    setBColor(buttonObject, cubeColoursList[colourValue])
    buttonObject.grid(column = columnNumber, row = rowNum, padx = padding, pady = padding)
    return listValue

#draw row of three squares
def createRow(columnNum, rowNum, startColourValue, listValue):
    for i in range(3):
        listValue = createOneSquare(columnNum + i, rowNum, startColourValue, listValue)
    return listValue

#draw three rows of three squares, whole face
def createSide(columnNum, rowNum, startColourValue, listValue):
    for i in range(3):
        listValue = createRow(columnNum, rowNum + i, startColourValue, listValue)
    return listValue

#draw all 6 sides
def createNewWhole():
    for widget in cubeInputFrame.winfo_children():
           widget.destroy()
    
    placeInList = 0
    placeInList = createSide(3, 0, 0, placeInList) #U1-U9
    placeInList = createSide(6, 3, 1, placeInList) #L1-L9
    placeInList = createSide(3, 3, 2, placeInList) #F1-F9
    placeInList = createSide(3, 6, 3, placeInList) #D1-D9
    placeInList = createSide(0, 3, 4, placeInList) #R1-R9
    placeInList = createSide(9, 3, 5, placeInList) #B1-B9
    
    outputText("Ready!")

def reset():
    createNewWhole()
    currentCube = list(jsonData["solvedCubeNotationList"])
    outputText(listToString(currentCube))

#solve the cube
def solve():
    
    start = time.time()
    
    try:
        mixString = listToString(currentCube)
        outputText("Solve function: " + mixString)
        solution = k.solve(mixString)
        outputText("Solution: " + solution)
    except ValueError:
        outputText("An error has occurred, please revise your \ninputs")
        
    algorithmList = solution.split()
    
    for i in range(len(algorithmList)):
        if algorithmList[i] == "U":
            UMotor.rotate(CC, quarterTurn)
        
        elif algorithmList[i] == "U'":
            UMotor.rotate(CCW, quarterTurn)
            
        elif algorithmList[i] == "U2":
            UMotor.rotate(CCW, halfTurn)
            
        elif algorithmList[i] == "L":
            LMotor.rotate(CC, quarterTurn)
        
        elif algorithmList[i] == "L'":
            LMotor.rotate(CCW, quarterTurn)
            
        elif algorithmList[i] == "L2":
            LMotor.rotate(CCW, halfTurn)
            
        elif algorithmList[i] == "R":
            RMotor.rotate(CC, quarterTurn)
        
        elif algorithmList[i] == "R'":
            RMotor.rotate(CCW, quarterTurn)
            
        elif algorithmList[i] == "R2":
            RMotor.rotate(CCW, halfTurn)
            
        elif algorithmList[i] == "D":
            DMotor.rotate(CC, quarterTurn)
        
        elif algorithmList[i] == "D'":
            DMotor.rotate(CCW, quarterTurn)
            
        elif algorithmList[i] == "D2":
            DMotor.rotate(CCW, halfTurn)
            
        elif algorithmList[i] == "F":
            FMotor.rotate(CC, quarterTurn)
        
        elif algorithmList[i] == "F'":
            FMotor.rotate(CCW, quarterTurn)
            
        elif algorithmList[i] == "F2":
            FMotor.rotate(CCW, halfTurn)
            
        elif algorithmList[i] == "B":
            BMotor.rotate(CC, quarterTurn)
        
        elif algorithmList[i] == "B'":
            BMotor.rotate(CCW, quarterTurn)
            
        elif algorithmList[i] == "B2":
            BMotor.rotate(CCW, halfTurn)
        
    end = time.time()
    outputText("Finished in: " + str(round(end - start, 3)))
        
#create button for solving cube
solveButton = Button(root, text = "Solve", padx = 20, pady = 5, command = solve)
solveButton.grid(column = 1, row = 1, padx = 5, pady = 2)

resetButton = Button(root, text = "Reset", padx = 20, pady = 5, command = reset)
resetButton.grid(column = 2, row = 1, padx = 5, pady = 2)

createNewWhole()

root.mainloop()