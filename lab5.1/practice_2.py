import RPi.GPIO as GPIO
import time
# to use raspberry PI GPIO numbers
GPIO.setmode (GPIO.BCM) # GPIO18 ,23,24,25 

# blinking funtion
def blink (pin1,pin2,pin3,pin4):
      # setup GPIO output channel
    GPIO.setup (pin1, GPIO.OUT)
    GPIO.setup (pin2, GPIO.OUT)
    GPIO.setup (pin3, GPIO.OUT)
    GPIO.setup (pin4, GPIO.OUT)

    GPIO.output (pin1, 1)
    GPIO.output (pin2, 1)
    GPIO.output (pin3, 1)
    GPIO.output (pin4, 1)

    time.sleep (0.5)

    GPIO.output (pin1, 0)
    GPIO.output (pin2, 0)
    GPIO.output (pin3, 0)
    GPIO.output (pin4, 0)

    time.sleep (0.5)  
      
    
try:
    while(1):
        blink (24,25,18,23)
except KeyboardInterrupt:
    GPIO.cleanup ()
    print ("program executed")