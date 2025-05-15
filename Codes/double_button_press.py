from machine import Pin
import time

button  = Pin(16, Pin.IN, Pin.PULL_DOWN)
last_time = 0

def check_button():
    click_count = 0
    start_time = time.ticks_ms()
    if button.value() == 1:
        click_count += 1
    while button.value() == 1:
        time.sleep(0.01)
    while True:
        now = time.ticks_ms()
        if now - start_time >= 500:
            break
        if button.value() == 1:
            click_count += 1
            while button.value() == 1:
                time.sleep(0.01)
            break
    return click_count


while True:
    while button.value() == 0:
        time.sleep(0.01)
    taps = check_button()
    if taps > 1:
        print("double tap")
    else:
        print("single tap")
    while button.value() == 1:
        time.sleep(0.01)