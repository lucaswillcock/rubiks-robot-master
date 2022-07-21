import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 96)

pixels.fill((100, 100, 100))