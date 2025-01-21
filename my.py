import pyfirmata
import time

my_port = 'COM9'
board = pyfirmata.Arduino(my_port)
pin9 = board.get_pin('d:10:s')

def move_servo(angle):
    pin9.write(angle)

try:
    while True:
        for angle in range(0, 181, 10):
            move_servo(angle)
            time.sleep(0.5)
        for angle in range(180, -1, -10):
            move_servo(angle)
            time.sleep(0.5)
except KeyboardInterrupt:
    board.exit()
