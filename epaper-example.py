#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd4in2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback


try:
    
    epd = epd4in2.EPD()
    epd.init()
    epd.Clear()
    
    font24 = ImageFont.truetype('Font.ttc', 24)
    font18 = ImageFont.truetype('Font.ttc', 18)
    font35 = ImageFont.truetype('Font.ttc', 35)
    
    # Drawing on the Horizontal image
    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), 'hello world', font = font24, fill = 0)
    draw.text((10, 20), '4.2inch e-Paper', font = font24, fill = 0)   
    draw.line((20, 50, 70, 100), fill = 0)
    draw.line((70, 50, 20, 100), fill = 0)
    draw.rectangle((20, 50, 70, 100), outline = 0)
    draw.line((165, 50, 165, 100), fill = 0)
    draw.line((140, 75, 190, 75), fill = 0)
    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
    draw.rectangle((80, 50, 130, 100), fill = 0)
    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)
    
    epd.Clear()
    epd.sleep()
    
except KeyboardInterrupt:    
    epd4in2.epdconfig.module_exit()
    exit()
