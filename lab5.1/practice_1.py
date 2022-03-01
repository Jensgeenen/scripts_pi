import RPi.GPIO as GPIO
import time
# to use raspberry PI GPIO numbers
GPIO.setmode (GPIO.BCM) # GPIO18 ,23,24,25 

# blinking funtion
def blink (pin1):
      # setup GPIO output channel
    GPIO.setup (pin1, GPIO.OUT)   

    GPIO.output (pin1, 1)   

    time.sleep (0.5)

    GPIO.output (pin1, 0)
       
    time.sleep (0.5)    
      
    
try:
    while(1):
        blink (24)
except KeyboardInterrupt:
    GPIO.cleanup ()
    print ("program executed")