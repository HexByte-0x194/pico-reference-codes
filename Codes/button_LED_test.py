from machine import Pin
import time

button  = Pin(15, Pin.IN, Pin.PULL_DOWN) # Set the button to connect to pin 15 as an input with a pull-down resistor
led = Pin(16, Pin.OUT) # Set pin to GPIO 16

while True:
    b_state  = button.value()
    print(b_state)
    led.value(b_state)
    time.sleep(0.1)