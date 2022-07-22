import cv2 as cv

def takePhoto(port, imageName):
        camera0 = cv.VideoCapture(port)
        _, image = camera0.read()
        #topImg = cv.flip(topImg, 1)
        cv.imwrite(imageName, image)
        print("Image capture successful")
        camera0.release()
        

takePhoto(1, "bottom.png")