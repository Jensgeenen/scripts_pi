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
        print ("buttom pressed")

        #short pulse
        GPIO.output (18, 1)
        time.sleep (0.5/6)
        GPIO.output (18, 0)  
        time.sleep (0.5/6)
        GPIO.output (18, 1)
        time.sleep (0.5/6)
        GPIO.output (18, 0)  
        time.sleep (0.5/6)
        GPIO.output (18, 1)
        time.sleep (0.5/6)
        GPIO.output (18, 0)  
        time.sleep (0.5/6)

        #long pulse
        GPIO.output (18, 1)
        time.sleep (0.25)
        GPIO.output (18, 0)  
        time.sleep (0.25)
        GPIO.output (18, 1)
        time.sleep (0.25)
        GPIO.output (18, 0)  
        time.sleep (0.25)
        GPIO.output (18, 1)
        time.sleep (0.25)
        GPIO.output (18, 0)  
        time.sleep (0.25)        
        
    else:
        GPIO.output (18, 1)
        print ("buttom release")
        time.sleep (0.3) 