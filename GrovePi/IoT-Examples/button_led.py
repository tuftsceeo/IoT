# button_led.py
# Purpose: to turn the LED on/off when button is pushed
# Date: July 21st, 2016
# By: Bianca Capretta

from grovepi import *
import time
import math

button = 3 # connect the button to digital port D3
led = 4 # Connect the LED to digital port D4

pinMode(led, "OUTPUT")  # Assign mode for LED as output
pinMode(button, "INPUT") # Assign mode for button as input

print ("Push the button to see the LED shine")
print (" ")
state = 0

while True:
        try:
                # Read if button is pushed or not
                button_status = digitalRead(button)

                # if button is pressed, switch state of light (ON/OFF)
                if button_status:
                        if state == 1:
                                state = 0  # LED off
                        elif state == 0:
                                state = 1  # LED on

                if state == 1:
                        print ("LED ON")
                        digitalWrite(led, 1)
                elif state == 0:
                        print ("LED OFF")
                        digitalWrite(led, 0)

                time.sleep(0.2)

        except KeyboardInterrupt:     # Turn LED off before stopping
                digitalWrite(led, 0)
                break
        except IOError:
                print("Error")
