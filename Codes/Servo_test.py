import time
from servo import Servo

my_servo = Servo(pin_id=0)

while True:
    my_servo.write(0)
    time.sleep(1)
    my_servo.write(180)
    time.sleep(1)
    my_servo.write(90)
    time.sleep(1)