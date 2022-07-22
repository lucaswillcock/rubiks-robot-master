import board
import neopixel
import I2C_LCD_driver
import RPi.GPIO as GPIO
import time

LCD = I2C_LCD_driver.lcd()

for i in range(4):
    delay = 0.2
    LCD.lcd_display_string("Booting Pi...  |", 1)
    time.sleep(delay)
    LCD.lcd_display_string("Booting Pi...  /", 1)
    time.sleep(delay)
    LCD.lcd_display_string("Booting Pi...  -", 1)
    time.sleep(delay)
    LCD.lcd_display_string("Booting Pi...  '\'", 1)
    time.sleep(delay)

Rmotor = 22
Bmotor = 5
Umotor = 6
Lmotor = 13
Dmotor = 19
Fmotor = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(Rmotor, GPIO.OUT)
GPIO.setup(Bmotor, GPIO.OUT)
GPIO.setup(Umotor, GPIO.OUT)
GPIO.setup(Lmotor, GPIO.OUT)
GPIO.setup(Dmotor, GPIO.OUT)
GPIO.setup(Fmotor, GPIO.OUT)

GPIO.output(Rmotor, 0)
GPIO.output(Bmotor, 0)
GPIO.output(Umotor, 0)
GPIO.output(Lmotor, 0)
GPIO.output(Dmotor, 0)
GPIO.output(Fmotor, 0)

pixels = neopixel.NeoPixel(board.D18, 96)

pixels.fill((255, 55, 55))

LCD.lcd_clear()
LCD.lcd_display_string("Welcome Lucas.", 1)