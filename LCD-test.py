import I2C_LCD_driver
import time

lcd = I2C_LCD_driver.lcd()

lcd.lcd_display_string("penis", 1)
time.sleep(20)

def displayTopLine(text):
    lcd.lcd_display_string("                ", 1)
    lcd.lcd_display_string(text, 1)
    
def displayBottomLine(text):
    lcd.lcd_display_string("                ", 17)
    lcd.lcd_display_string(text, 17)
    

displayTopLine("Top text")
displayBottomLine("bottom text")