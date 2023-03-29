import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(bit) for bit in format(value, 'b').zfill(8)]

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

DAC     = [26, 19, 13, 6, 5, 11, 9, 10]
# AUX     = [2, 3, 14, 15, 18, 27, 23, 22]

GPIO.setup(DAC, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)


PWM = GPIO.PWM(2, 1000)


try: 
    while True:
        value = input()

        try:
            value = int(value)
        except ValueError:
            print("==INPUT=ERROR== '", value, "' expected to be [0-255]")
            break
            
        if value < 0 or value > 100:
            print("==INPUT=ERROR== '", value, "' expected to be [0-255]")
            break

        PWM.start(value)
     
finally:
    GPIO.output(2, 0)
    PWM.stop()
    GPIO.cleanup()