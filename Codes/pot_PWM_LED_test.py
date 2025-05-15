from machine import Pin, PWM, ADC
import time

pwm_pin = PWM(Pin(16))
pot = ADC(Pin(26))

pwm_pin.freq(1000)
conversion_factor = 3.3 / 65535

while True:
    pot_voltage = pot.read_u16()
    pwm_pin.duty_u16(pot_voltage)
    print(pot_voltage * conversion_factor)
    time.sleep(0.05)