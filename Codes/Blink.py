from machine import Pin
import time

led = Pin(16, Pin.OUT) # Set pin to GPIO 16

while True:       # Loop infinitely
    led.value(1)   # Turn the LED on
    time.sleep(2)  # Wait for 2 seconds
    
    led.value(0)   # Turn the LED off
    time.sleep(2)  # Wait for 2 seconds