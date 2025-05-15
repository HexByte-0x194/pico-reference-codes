from machine import Pin, ADC
import time

pot = ADC(Pin(26))

conversion_factor = 3.3 / 65535

while True:
    pot_voltage = pot.read_u16() * conversion_factor
    
    print(pot_voltage)
    time.sleep(0.1)