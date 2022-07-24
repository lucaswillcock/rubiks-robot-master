import cv2 as cv
import ledssss
import time

brightness = 20
white = (brightness, brightness, brightness)

ringBack = ledssss.ledRing(1)
ringUp = ledssss.ledRing(2)
ringLeft = ledssss.ledRing(3)
ringDown = ledssss.ledRing(4)
ringRight = ledssss.ledRing(5)
ringFront = ledssss.ledRing(6)

def takePhoto(port, imageName):
        camera0 = cv.VideoCapture(port)
        _, image = camera0.read()
        cv.imwrite(imageName, image)
        print("Image capture successful")
        camera0.release()
        

def photoTop():
    ringBack.on(white)
    ringUp.on(white)
    ringLeft.on(white)
    ringRight.off()
    ringDown.off()
    ringFront.off()
    time.sleep(0.2)
    takePhoto(2, "top.png")
    time.sleep(0.2)
    
def photoBottom():
    ringRight.on(white)
    ringDown.on(white)
    ringFront.on(white)
    ringBack.off()
    ringUp.off()
    ringLeft.off()
    time.sleep(0.2)
    takePhoto(0, "bottom.png")
    time.sleep(0.2)
    
photoBottom()
photoTop()