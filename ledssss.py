import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 96)

pixels.fill((255, 255, 255))

time.sleep(1)

pixels.fill((0, 0, 0))


for i in range(10):
    for i in range(96):
        
        pixels[i] = (i, i, 255)
        time.sleep(0.1)
        pixels[i] = (0, 0 ,0)