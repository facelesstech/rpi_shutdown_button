# Button connected to pin 15
# LED connected to pin 16

import RPi.GPIO as GPIO
from subprocess import call
import time

GPIO.setmode(GPIO.BOARD) # Set GPIO mode
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set up pin 15 as an input with pull up resistor

GPIO.setup(16, GPIO.OUT) # Set up pin 16 as an output

def watchForButton(pin):

    if not (GPIO.input(pin)):
        GPIO.output(16, True) # Turn on LED
        call(['shutdown', '-h', 'now'], shell=False) # Send shutdown command

GPIO.add_event_detect(15, GPIO.BOTH, callback=watchForButton) # Watch for change

while True:
    # sleep to reduce unnecessary CPU usage
    time.sleep(5)
