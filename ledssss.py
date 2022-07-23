import board
import neopixel
import time

leds = neopixel.NeoPixel(board.D18, 96)

# leds.fill((255, 255, 255))

class ledRing:
    def __init__(self, motorNum):
        self.pixels = []
        for i in range(16):
            self.pixels.append(((motorNum-1) * 16) + i)
            
    def on(self, colour):
        for i in range(len(self.pixels)):
            leds[self.pixels[i]] = colour
            
    def off(self):
        for i in range(len(self.pixels)):
            leds[self.pixels[i]] = (0,0,0)
            
            
ringBack = ledRing(1)
ringUp = ledRing(2)
ringLeft = ledRing(3)
ringDown = ledRing(4)
ringRight = ledRing(5)
ringFront = ledRing(6)

ringBack.on((0, 0, 60))
ringUp.on((20, 20, 20))
ringLeft.on((50, 10, 0))
ringDown.on((30, 30, 0))
ringRight.on((60, 0, 0))
ringFront.on((0, 60, 0))
