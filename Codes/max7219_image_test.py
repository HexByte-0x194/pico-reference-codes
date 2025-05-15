import max7219
from machine import Pin, SPI
from time import sleep

# SPI Setup
spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(14), mosi=Pin(15))
ss = Pin(13, Pin.OUT)

# Set up display with 1 matrix
display = max7219.Matrix8x8(spi, ss, 1)
display.brightness(1)   # Adjust brightness 1 to 15

# Smiley face 8x8 bitmap (0 = off, 1 = on)
smiley_face = [
    [0, 0, 1, 1, 1, 1, 0, 0],  # Top row
    [0, 1, 1, 0, 0, 1, 1, 0],  # Empty row
    [1, 1, 1, 0, 0, 0, 1, 1],  # Eye row
    [1, 0, 0, 1, 0, 0, 0, 1],  # Empty row
    [1, 0, 0, 0, 1, 0, 0, 1],  # Mouth row
    [1, 1, 0, 0, 0, 1, 1, 1],  # Empty row
    [0, 1, 1, 0, 0, 1, 1, 0],  # Empty row
    [0, 0, 1, 1, 1, 1, 0, 0]   # Empty row
]

# Clear display before drawing
display.fill(0)
display.show()

# Draw smiley face on the matrix
for y in range(8):
    for x in range(8):
        # If the pixel is part of the smiley face (1), turn it on
        display.pixel(x, y, smiley_face[y][x])

# Update the display to show the smiley face
display.show()

# Keep the smiley face displayed for 5 seconds
sleep(5)
