from machine import UART, Pin
from time import sleep

test_uart = UART(1, baudrate = 9600, tx=Pin(4))

while True:
        test_uart.write("ON")
        sleep(2)
        test_uart.write("OFF")
        sleep(2)
