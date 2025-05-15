import max7219
from machine import Pin, SPI
from time import sleep
spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(14), mosi=Pin(15))
ss = Pin(13, Pin.OUT)

msg = 'T'
display = max7219.Matrix8x8(spi, ss, 1)
display.brightness(1)   # adjust brightness 1 to 15
display.fill(0)
display.show()
sleep(0.5)

display.text(msg ,0,0,1)
display.show()
sleep(5)
display.fill(0)
display.show()