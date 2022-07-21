import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 96)

pixels.fill((255, 255, 255))

time.sleep(1)

pixels.fill((50,50,50))


for i in range(10):
    for i in range(96):
        
        pixels[i] = (255, 255, 255)
        time.sleep(0.1)
        pixels[i] = (0, 0 ,0)