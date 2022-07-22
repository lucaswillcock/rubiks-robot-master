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
            leds[self.pixels[i]] = colour
            
    def off(self):
        for i in range(len(self.pixels)):
            leds[self.pixels[i]] = (0,0,0)
            
            
ringBack = ledRing(1)
ring2 = ledRing(2)
ring3 = ledRing(3)
ring4 = ledRing(4)
ring5 = ledRing(5)
ring6 = ledRing(6)

ringBack.on((0, 50, 0))
ring2.on((0, 50, 0))
ring3.on((0, 50, 0))
ring4.on((0, 50, 0))
ring5.on((0, 50, 0))
ring6.on((0, 50, 0))