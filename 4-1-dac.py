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

try: 
    while True:
        value = input()

        try:
            value = int(value)
        except ValueError:
            print("==INPUT=ERROR== '", value, "' expected to be [0-255]")
            break
            
        if value < 0 or value > 255:
            print("==INPUT=ERROR== '", value, "' expected to be [0-255]")
            break

        BinValue = decimal2binary(value)
        print("voltage is ", 3.3*value/256, "")
        GPIO.output(DAC, BinValue)
        
finally:
    GPIO.output(DAC, 0)
    GPIO.cleanup()