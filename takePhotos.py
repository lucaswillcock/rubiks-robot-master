import cv2 as cv

def takePhoto(port, imageName):
        camera0 = cv.VideoCapture(port)
        _, image = camera0.read()
        cv.imwrite(imageName, image)
        print("Image capture successful")
        camera0.release()
        

takePhoto(2, "top.png")
takePhoto(0, "bottom.png")