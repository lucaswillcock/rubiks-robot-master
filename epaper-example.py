#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

from waveshare_epd import epd4in2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback


try:
    
    display = epd4in2.EPD()
    print("initialising")
    display.init()
    print("clearing")
    display.Clear()
    
    font24 = ImageFont.truetype('Font.ttc', 24)
    font18 = ImageFont.truetype('Font.ttc', 18)
    font35 = ImageFont.truetype('Font.ttc', 35)
    
    # Drawing on the Horizontal image
    Himage = Image.new('1', (display.width, display.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), 'My nuts are huge', font = font35, fill = 0)  
    #draw.line((20, 50, 70, 100), fill = 0)
    print("display image")
    display.display(display.getbuffer(Himage))
    time.sleep(10)
    print("clearing")
    display.Clear()
    display.sleep()
    
except KeyboardInterrupt:    
    epd4in2.epdconfig.module_exit()
    exit()
