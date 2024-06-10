import RPi.GPIO as GPIO
from time import sleep


def doorunlock():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, 0)
    sleep(3)
    GPIO.output(12, 1)
    GPIO.cleanup()
    
    
def doorlock():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    sleep(0.5)
    GPIO.cleanup()
