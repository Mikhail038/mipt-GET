import RPi.GPIO as GPIO
import time



DAC = [26, 19, 13, 6, 5, 11, 9, 10]
BinNumber = [0, 0, 0, 0, 0, 0, 0, 0]


GPIO.setmode (GPIO.BCM)
GPIO.setup (DAC,GPIO.OUT)

GPIO.output(DAC, 0)

a = 5

BinNumber = [1, 1, 1, 1, 1, 1, 1, 0]
GPIO.output(DAC, BinNumber)
time.sleep(a)
GPIO.output(DAC, 0)

BinNumber = [0, 1, 1, 1, 1, 1, 1, 1]
GPIO.output(DAC, BinNumber)
time.sleep(a)
GPIO.output(DAC, 0)

BinNumber = [0, 1, 0, 0, 0, 0, 0, 0]
GPIO.output(DAC, BinNumber)
time.sleep(a)
GPIO.output(DAC, 0)

BinNumber = [0, 0, 1, 0, 0, 0, 0, 0]
GPIO.output(DAC, BinNumber)
time.sleep(a)
GPIO.output(DAC, 0)

BinNumber = [0, 0, 0, 0, 0, 1, 0, 1]
GPIO.output(DAC, BinNumber)
time.sleep(a)
GPIO.output(DAC, 0)

BinNumber = [0, 0, 0, 0, 0, 0, 0, 0]
GPIO.output(DAC, BinNumber)
time.sleep(a)
GPIO.output(DAC, 0)

BinNumber = [0, 0, 0, 0, 0, 0, 0, 0]
GPIO.output(DAC, BinNumber)
time.sleep(a)
GPIO.output(DAC, 0)

# for i in range (0,25):
#     for led in LEDs:
#         GPIO.output(led, 1)
#         time.sleep(0.a)
#         GPIO.output(led,0)

GPIO.output(DAC, 0)
GPIO.cleanup()