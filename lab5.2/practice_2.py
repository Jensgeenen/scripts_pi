# event input 
import RPi.GPIO as GPIO
import time
GPIO.cleanup ()
# to use raspberry PI board GPIO numbers
GPIO.setmode (GPIO.BCM)
GPIO.setup (17, GPIO.IN) # GPIO 17 input
GPIO.setup(18, GPIO.OUT) # GPIO 18 output
# loop forever or ctrl^C
while True:
    if (GPIO.input (17)==0): #input low active
        print ("button pressed")
        GPIO.output (18, 0)        
        time.sleep (0.3) # anti bouncing
    else:
        print ("button release")       
        GPIO.output (18, 1)
        time.sleep (0.3) # anti bouncing
        GPIO.output (18, 0)
        time.sleep (0.3) # anti bouncing
