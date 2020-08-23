#import RPi.GPIO as gpio
import time

def GPIO_output(a, b):
    print("pin " + str(a) + " set to " + str(b))


class motor:
    def __init__(self, enable, clock, direction, delay):
        self.en = enable
        self.clk = clock
        self.dir = direction
        self.dly = delay
        
        GPIO_output(self.en, "high")
        
    def rotate(self, direction, distance):
        GPIO_output(self.en, "low")
        GPIO_output(self.dir, "high")
        for i in range(50):
            GPIO_output(self.clk, "high")
            time.sleep(self.dly)
            GPIO_output(self.clk, "low")
            time.sleep(self.dly)
            
        GPIO_output(self.en, "high")
    
Motor = motor("enable", "clock", "direction", 0.02)

Motor.rotate("high", 50)