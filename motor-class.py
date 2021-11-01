import RPi.GPIO as GPIO
import time

enable_PIN = 4
pulse_PIN = 21
direction_PIN = 27

GPIO.setmode(GPIO.BCM)

class motor:
    def __init__(self, enable, clock, direction, delay):
        self.en = enable
        self.clk = clock
        self.dir = direction
        self.dly = delay
        
        GPIO.setup(enable, GPIO.OUT)
        GPIO.setup(clock, GPIO.OUT)
        GPIO.setup(direction, GPIO.OUT)
        
        GPIO.output(self.en, 1)
        
    def rotate(self, direction, distance):
        GPIO.output(self.en, 0)
        GPIO.output(self.dir, 1)
        for i in range(50):
            GPIO.output(self.clk, 1)
            time.sleep(self.dly)
            GPIO.output(self.clk, 0)
            time.sleep(self.dly)
            
        GPIO.output(self.en, 1)
    
speed = 0.02

Motor = motor(enable_PIN, pulse_PIN, direction_PIN, speed)

while 1:
    speed = input("Speed: ")
    Motor.rotate("high", 50)
    print("Finished")