import I2C_LCD_driver as LCD
import RPi.GPIO as GPIO

buttonPin = 27

GPIO.setmode(GPIO.BCM)

lcd = LCD.lcd()

GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while 1:
    if GPIO.input(buttonPin) == GPIO.HIGH:
        lcd.lcd_display_string("Button pressed", 1)