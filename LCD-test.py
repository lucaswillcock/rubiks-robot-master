import I2C_LCD_driver
import time

lcd = I2C_LCD_driver.lcd()

def displayTopLine(text):
    lcd.lcd_display_string("                ", 1)
    lcd.lcd_display_string(text, 1)
    
def displayBottomLine(text):
    lcd.lcd_display_string("                ", 2)
    lcd.lcd_display_string(text, 2)
    

displayTopLine("Top text")
displayBottomLine("bottom text")