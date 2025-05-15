from machine import Pin
import time

button  = Pin(16, Pin.IN, Pin.PULL_DOWN) # Set the button to connect to pin 15 as an input with a pull-down resistor

while True:
    print(button.value())
    time.sleep(0.1)