import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 96)

pixels[0] = (255, 255, 255)