import RPi.GPIO as GPIO
import time
import I2C_LCD_driver as LCD
GPIO.setmode(GPIO.BCM)

lcd = LCD.lcd()

lcd.lcd_clear()
lcd.lcd_display_string("Hello mum!", 1)

pulseDelay = 0.0002

pulse = 27
direction = 17

Rmotor = 22
Bmotor = 5
Umotor = 6
Lmotor = 13
Dmotor = 19
Fmotor = 26

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
        GPIO.output(self.dir, 1)
        for i in range(distance):
            GPIO.output(self.pulse, 1)
            time.sleep(self.dly)
            GPIO.output(self.pulse, 0)
            time.sleep(self.dly)
            
        time.sleep(0.01)
        GPIO.output(self.en, 0)
        
MotorRight = motor(Rmotor, pulse, direction, pulseDelay)
MotorBack = motor(Bmotor, pulse, direction, pulseDelay)
MotorUp = motor(Umotor, pulse, direction, pulseDelay)
MotorLeft = motor(Lmotor, pulse, direction, pulseDelay)
MotorDown = motor(Dmotor, pulse, direction, pulseDelay)
MotorFront = motor(Fmotor, pulse, direction, pulseDelay)

def runAll():
    
    MotorRight.rotate(1, 400)
    MotorLeft.rotate(1, 400)
    MotorUp.rotate(1, 400)
    MotorDown.rotate(1, 400)
    MotorFront.rotate(1, 400)
    MotorBack.rotate(1, 400)
    
for i in range(2):
    runAll()