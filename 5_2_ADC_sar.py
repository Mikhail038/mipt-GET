import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(bit) for bit in format(value, 'b').zfill(8)]

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    for value in range(256):
        signal = dec2bin(value)
        GPIO.output(DAC, signal)
        time.sleep(0.001)
        compValue = GPIO.input(comp)
        if compValue == 0:
            return value

    return value

def adc2():
    value = 0
    delta = 128
    while True:
        value += int(delta)

        signal = dec2bin(int (value))
        GPIO.output(DAC, signal)
        time.sleep(0.001)

        compValue = GPIO.input(comp)
        if compValue == 1:
            if delta == 1:
                return value  
            delta = int(delta/2) 
        else:
            value -= delta
            if delta == 1:
                return value  
            delta = int(delta/2) 
            
        

GPIO.setmode(GPIO.BCM)

DAC     = [26, 19, 13, 6, 5, 11, 9, 10]

maxVoltage = 3.3

troyka  = 17
comp    = 4


GPIO.setup(DAC, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


try: 
    while True:

            value = adc2()
            voltage = (value / 256) * maxVoltage

            print("input voltage = {:.2f}".format(voltage))



finally:
    GPIO.output(DAC, GPIO.LOW)
    GPIO.output(troyka, 0)

    GPIO.cleanup()