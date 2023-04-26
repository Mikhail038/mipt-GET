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

t = input()

try:
    t = float(t)
except ValueError:
    print("==INPUT=ERROR== '", t, "' expected to be [float]")

t =  t / (256 *2)
i = 1
value = 0

try: 
    while True:
        value = value + i

        BinValue = decimal2binary(value)
        print("voltage is ", 3.3*value/256, "")
        GPIO.output(DAC, BinValue)
        time.sleep(t)

        if value <= 0:
            i = 1
                
        if value >= 255: 
            i = -1
            
finally:
    GPIO.output(DAC, 0)
    GPIO.cleanup()