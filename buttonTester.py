import I2C_LCD_driver as LCD
import RPi.GPIO as GPIO

buttonPin = 27

GPIO.setmode(GPIO.BCM)

lcd = LCD.lcd()

GPIO.setmode(buttonPin, GPIO.IN)

while 1:
    if GPIO.input(buttonPin) == GPIO.HIGH:
        lcd.lcd_display_string("Button pressed", 1)