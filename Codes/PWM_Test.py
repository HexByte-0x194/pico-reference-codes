from machine import Pin, PWM

pwm_pin = PWM(Pin(16))

max = 65535

pwm_pin.freq(1000)

while True:
    PWM_value = int(0.5 * max)
    
    pwm_pin.duty_u16(PWM_value)