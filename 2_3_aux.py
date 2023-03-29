import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LEDs    = [24, 25, 8, 7, 12, 16, 20, 21]
AUX     = [2, 3, 14, 15, 18, 27, 23, 22]

GPIO.setup(LEDs, GPIO.OUT)
GPIO.setup(AUX, GPIO.IN)

while True:
    for i in range(0,7):
        GPIO.output(LEDs[i], GPIO.input(AUX[i]))

GPIO.cleanup()