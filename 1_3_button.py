import RPi.GPIO as RIO

RIO.setmode(RIO.BCM)

RIO.setup(27, RIO.IN)
RIO.setup(22, RIO.OUT)

while True:
    RIO.output(22, RIO.input(27))



