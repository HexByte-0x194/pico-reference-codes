from machine import Pin
import time

button  = Pin(15, Pin.IN, Pin.PULL_DOWN) # Set the button to connect to pin 15 as an input with a pull-down resistor
led = Pin(16, Pin.OUT) # Set pin to GPIO 16
timer = 0

while True:
    time.sleep(1)
    if button.value() == 1:
        timer = timer + 1
        print(timer)