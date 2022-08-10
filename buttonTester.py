import I2C_LCD_driver as lcd
import RPi.GPIO as GPIO

buttonPin = 21

GPIO.setmode(GPIO.BCM)

lcd = lcd.lcd()

GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

print(GPIO.input(buttonPin))

lcd.lcd_display_string("Button not pressed", 1)

while 1:
    print(GPIO.input(buttonPin))
    if GPIO.input(buttonPin) == GPIO.HIGH:
        lcd.lcd_display_string("Button pressed", 1)