import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 96)

pixels.fill((255, 255, 255))

time.sleep(1)

pixels.fill((50,50,50))