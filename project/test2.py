import RPi.GPIO as GPIO
import time
switch1 = 0
switch2 = 0
switch3 = 0

# to use raspberry PI board GPIO numbers
GPIO.setmode (GPIO.BCM)
GPIO.setup (17, GPIO.IN) # GPIO 17 input
GPIO.setup(18, GPIO.OUT) # GPIO 18 output
GPIO.setup (27, GPIO.IN) 
GPIO.setup(23, GPIO.OUT) 
GPIO.setup (22, GPIO.IN) 
GPIO.setup(24, GPIO.OUT) 
# loop forever or ctrl^C
try:
    while (True):
        if (GPIO.input (17)==0): #input low active
            if (switch1 == 0):
                print ("buttom 1 pressed")
                GPIO.output (18, 1)
                switch1 = 1
                time.sleep (0.3)
            else: 
                GPIO.output (18, 0)
                print ("buttom 1 release")
                switch1 = 0
                time.sleep (0.3)

        elif (GPIO.input (27)==0): #input low active
            if (switch2 == 0):
                print ("buttom 2 pressed")
                GPIO.output (23, 1)
                switch2 = 1
                time.sleep (0.3)
            else: 
                GPIO.output (23, 0)
                print ("buttom 2 release")
                switch2 = 0
                time.sleep (0.3)

        elif (GPIO.input (22)==0): #input low active
            if (switch3 == 0):
                print ("buttom 3 pressed")
                GPIO.output (24, 1)
                switch3 = 1
                time.sleep (0.3)
            else: 
                GPIO.output (24, 0)
                print ("buttom 3 release")
                switch3 = 0
                time.sleep (0.3)
                
except KeyboardInterrupt:
    #cleanup
    GPIO.cleanup()
    print("clean closed")     
