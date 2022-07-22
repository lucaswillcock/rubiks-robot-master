import board
import neopixel
import time

leds = neopixel.NeoPixel(board.D18, 96)

leds.fill((255, 255, 255))

class ledRing:
    def __init__(self, motorNum):
        self.pixels = []
        for i in range(16):
            self.pixels.append(i*motorNum)
            
    def on(self, colour):
        for i in range(len(self.pixels)):
            leds[self.pixels[i-1]] = colour
            
            
            
            
            
ringBack = ledRing(1)

ringBack.on((0, 50, 0))