import RPi.GPIO as GPIO
import time
# to use raspberry PI GPIO numbers
GPIO.setmode (GPIO.BCM) # GPIO18 ,23,24,25 

# blinking funtion
def blink (pin1):
      # setup GPIO output channel
    GPIO.setup (pin1, GPIO.OUT)   
    #short pulse
    GPIO.output (pin1, 1)
    time.sleep (0.5/6)
    GPIO.output (pin1, 0)  
    time.sleep (0.5/6)
    GPIO.output (pin1, 1)
    time.sleep (0.5/6)
    GPIO.output (pin1, 0)  
    time.sleep (0.5/6)
    GPIO.output (pin1, 1)
    time.sleep (0.5/6)
    GPIO.output (pin1, 0)  
    time.sleep (0.5/6)

    #long pulse
    GPIO.output (pin1, 1)
    time.sleep (0.25)
    GPIO.output (pin1, 0)  
    time.sleep (0.25)
    GPIO.output (pin1, 1)
    time.sleep (0.25)
    GPIO.output (pin1, 0)  
    time.sleep (0.25)
    GPIO.output (pin1, 1)
    time.sleep (0.25)
    GPIO.output (pin1, 0)  
    time.sleep (0.25)
    
    #short pulse
    GPIO.output (pin1, 1)
    time.sleep (0.5/6)
    GPIO.output (pin1, 0)  
    time.sleep (0.5/6)
    GPIO.output (pin1, 1)
    time.sleep (0.5/6)
    GPIO.output (pin1, 0)  
    time.sleep (0.5/6)
    GPIO.output (pin1, 1)
    time.sleep (0.5/6)
    GPIO.output (pin1, 0)  
    time.sleep (0.5/6)

                
      
    
try:
    while(1):
        blink (18)
except KeyboardInterrupt:
    GPIO.cleanup ()
    print ("program executed")