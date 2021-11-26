from pyfirmata import Arduino
import time

board = Arduino("/dev/tty.usbserial-142140")
print("Communication Successfully started")
    
for i in range(200):
    board.digital[13].write(1)
    time.sleep(0.1)
    board.digital[13].write(0)
    time.sleep(0.1)