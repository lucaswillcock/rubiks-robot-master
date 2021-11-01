import RPi.GPIO as GPIO
import time

enable_PIN = 1
pulse_PIN = 1
direction_PIN = 1

class motor:
    def __init__(self, enable, clock, direction, delay):
        self.en = enable
        self.clk = clock
        self.dir = direction
        self.dly = delay
        
        GPIO.output(self.en, "high")
        
    def rotate(self, direction, distance):
        GPIO.output(self.en, "low")
        GPIO.output(self.dir, "high")
        for i in range(50):
            GPIO.output(self.clk, "high")
            time.sleep(self.dly)
            GPIO.output(self.clk, "low")
            time.sleep(self.dly)
            
        GPIO.output(self.en, "high")
    
speed = 0.02

Motor = motor(enable_PIN, pulse_PIN, direction_PIN, speed)

while 1:
    speed = int(input("Speed: "))
    Motor.rotate("high", 50)
    print("Finished")