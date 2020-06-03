from machine import Pin
import _thread
from time import sleep

GPIO4 = Pin(4, Pin.OUT)
GPIO5 = Pin(5, Pin.OUT)



def blink(GPIO, interval):
    for i in range(1, 20, 1):
        GPIO.on()
        sleep(interval)
        GPIO.off()
        sleep(interval)
    

_thread.start_new_thread(blink, (GPIO4, 1))
_thread.start_new_thread(blink, (GPIO5, 0.3))    
