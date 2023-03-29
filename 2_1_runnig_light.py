import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LEDs = [24, 25, 8, 7, 12, 16, 20, 21]


GPIO.setup(LEDs, GPIO.OUT)

for i in range (0,3):
    for led in LEDs:
        GPIO.output(led, 1)
        time.sleep(0.2)
        GPIO.output(led,0)

GPIO.cleanup()