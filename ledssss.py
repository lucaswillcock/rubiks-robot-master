import board
import neopixel

leds = neopixel.NeoPixel(board.D18, 96)

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