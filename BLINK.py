from machine import Pin
from  utime import sleep
led=Pin(15,Pin.OUT)
while True:
     led.value(1)
     sleep(1)
     led.value(0)
     sleep(1)
     
     