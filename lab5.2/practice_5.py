import RPi.GPIO as GPIO
import time
GPIO.cleanup ()
# to use raspberry PI board GPIO numbers
GPIO.setmode (GPIO.BCM)
GPIO.setup (17, GPIO.IN) # GPIO 17 input
GPIO.setup (18, GPIO.OUT) # GPIO 18 output
GPIO.setup (23, GPIO.OUT)
GPIO.setup (24, GPIO.OUT)
GPIO.setup (25, GPIO.OUT)

# loop forever or ctrl^C
while True:
    if (GPIO.input (17)==0): #input low active
        print ("buttom pressed")
        GPIO.output (18, 1)
        GPIO.output (23, 0)
        GPIO.output (24, 0)
        GPIO.output (25, 0)    

        time.sleep (0.5)

        GPIO.output (18, 0)
        GPIO.output (23, 1)
        
        time.sleep (0.5)
        
        GPIO.output (23, 0)
        GPIO.output (24, 1)    

        time.sleep (0.5)
        
        GPIO.output (24, 0)
        GPIO.output (25, 1)

        time.sleep (0.5)
        
        GPIO.output (24, 1)
        GPIO.output (25, 0)

        time.sleep (0.5)
        
        GPIO.output (23, 1)
        GPIO.output (24, 0)
        
        time.sleep (0.5)  

    else:
        GPIO.output (18, 0)
        GPIO.output (23, 0)
        GPIO.output (24, 0)
        GPIO.output (25, 0)   
        print ("buttom release")
        time.sleep (0.3) # anti bouncing