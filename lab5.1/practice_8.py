# blink LED /home/pi
from turtle import delay
import RPi.GPIO as GPIO
import time
# to use raspberry PI GPIO numbers
GPIO.setmode (GPIO.BCM) # GPIO18
# blinking function
def blink(pin1, pin2, pin3, pin4, aantalBlinks, periode, dutyCycle):
      # setup GPIO output channel
    GPIO.setup (pin1, GPIO.OUT)
    GPIO.setup (pin2, GPIO.OUT)
    GPIO.setup (pin3, GPIO.OUT)
    GPIO.setup (pin4, GPIO.OUT)
    tijdhoog = periode * dutyCycle/100 
    tijdlaag = periode - tijdhoog
    for teller in range (0, aantalBlinks):
        GPIO.output (pin1, GPIO.HIGH)
        GPIO.output (pin2, GPIO.HIGH)
        GPIO.output (pin3, GPIO.HIGH)
        GPIO.output (pin4, GPIO.HIGH)
        time.sleep (tijdhoog)
        GPIO.output (pin1, GPIO.LOW)
        GPIO.output (pin2, GPIO.LOW)
        GPIO.output (pin3, GPIO.LOW)
        GPIO.output (pin4, GPIO.LOW)
        time.sleep (tijdlaag)
#main program blink GPIO18 (pin12) 10 times
blink(18,23,24,25, 200, 0.01, 25)
blink(18,23,24,25, 200, 0.01, 50)
blink(18,23,24,25, 200, 0.01, 75)
blink(18,23,24,25, 200, 0.01, 100)

# cleanup
GPIO.cleanup ()
print ("program executed")