
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time

amount = 10000
freq = 0.001

measured_data = [0] * amount
 
if __name__ == "__main__": 
    def decimal2binary(value):
        return [int(bit) for bit in format(value, 'b').zfill(8)]

    def dec2bin(value):
        return [int(element) for element in bin(value)[2:].zfill(8)]

    def adc():
        for value in range(256):
            signal = dec2bin(value)
            GPIO.output(DAC, signal)
            time.sleep(freq)
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
    LEDs    = [24, 25, 8, 7, 12, 16, 20, 21]

    maxVoltage = 3.3

    troyka  = 17
    comp    = 4


    GPIO.setup(DAC, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(LEDs, GPIO.OUT)
    GPIO.setup(comp, GPIO.IN)

    GPIO.setup(troyka, GPIO.OUT)


    GPIO.output(troyka, 0)

    try: 
        while adc2() != 0:
            time.sleep(0.1)

        start_t = time.time()

        for j in range (amount):

            value = adc2()  

            for i in range(0,7):
                if (256/8)*i < value:
                    GPIO.output(LEDs[i], 1)
                else:
                    GPIO.output(LEDs[i], 0)
                
            voltage = (value / 256) * maxVoltage

            if voltage >= 3.2:
                GPIO.output(troyka, 1)




            # print("input voltage = {:.2f}".format(voltage))
            print(j)

            measured_data[j] = voltage


            # open ()

        plt.plot (measured_data)
        plt.show ()

        measured_data_str = [str(item) for item in measured_data]

        with open ("7_data.txt", "w") as outfile:
            outfile.write ("\n".join (measured_data_str))

        with open ("7_settings.txt", "w") as outfile:
            outfile.write ("frequency (delta T): ")
            outfile.write (freq)
            outfile.write ("\n")

            outfile.write ("delta U: ")
            outfile.write (1/256)
            outfile.write ("\n")

            outfile.write ("Time passed: ")
            outfile.write (time.time() - start_t)
            outfile.write ("\n")


    finally:
        GPIO.output(DAC, GPIO.LOW)
        GPIO.output(troyka, 0)

        GPIO.cleanup()