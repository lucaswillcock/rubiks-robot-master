import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pulse = 27

class motor:
    def __init__(self, enable, pulse, direction, delay):
        self.en = enable
        self.pulse = pulse
        self.dir = direction
        self.dly = delay
        
        GPIO.setup(enable, GPIO.OUT)
        GPIO.setup(pulse, GPIO.OUT)
        GPIO.setup(direction, GPIO.OUT)
        
    def rotate(self, direction, distance):
        GPIO.output(self.en, 1)
        GPIO.output(self.dir, 1)
        for i in range(50):
            GPIO.output(self.pulse, 1)
            time.sleep(self.dly)
            GPIO.output(self.pulse, 0)
            time.sleep(self.dly)
            
        GPIO.output(self.en, 0)
        
motor1 = motor(22, pulse, 17, 0.005)

motor1.rotate(1, 400)