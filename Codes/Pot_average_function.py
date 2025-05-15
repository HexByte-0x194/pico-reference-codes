from machine import ADC, Pin
import time

pot = ADC(Pin(26))
conversion_factor = 100 / 65535

def read_pot():
    var1 = pot.read_u16()
    var2 = pot.read_u16()
    var3 = pot.read_u16()
    var4 = pot.read_u16()
    var5 = pot.read_u16()
    total = (var1 + var2 + var3 + var4 + var5) / 5
    return total

while True:
    print("Average:", read_pot(), "Raw: ", pot.read_u16())
    time.sleep(0.2)