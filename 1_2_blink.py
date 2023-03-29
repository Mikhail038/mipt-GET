import RPi.GPIO as RIO
import time

RIO.setmode(RIO.BCM)

RIO.setup(22, RIO.OUT)

while True:
    RIO.output(22, 1)
    time.sleep(1)
    RIO.output(22, 0)
    time.sleep(0.5)



