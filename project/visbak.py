import RPi.GPIO as GPIO
import time
teller = 0
GPIO.cleanup ()
# to use raspberry PI board GPIO numbers
GPIO.setmode (GPIO.BCM)
GPIO.setup (17, GPIO.IN)  # input depth
GPIO.setup (25, GPIO.IN)  # input light
GPIO.setup (23, GPIO.IN)  # input pomp
GPIO.setup (24, GPIO.IN)  # input voeder
GPIO.setup (18, GPIO.OUT) # output depth
GPIO.setup (27, GPIO.OUT) # output light
GPIO.setup (22, GPIO.OUT) # output pomp
GPIO.setup (5, GPIO.OUT)  # output step1
GPIO.setup (6, GPIO.OUT)  # output step2
GPIO.setup (26, GPIO.OUT) # output step3
GPIO.setup (16, GPIO.OUT) # output step4

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.IN)

try:
    while(True):
        GPIO.output(17, 1)
        time.sleep(0.00001)
        GPIO.output(17, 0)

        while(GPIO.input(18) == 0):
            pass

        signalHigh = time.time()

        while(GPIO.input(18) == 1):
            pass

        signalLow = time.time()
        timePassed = signalLow - signalHigh
        distance = 17000 * timePassed
        print(str(distance))
        time.sleep(0.5)

except KeyboardInterrupt:
    #cleanup
    GPIO.cleanup()
    print("clean closed")