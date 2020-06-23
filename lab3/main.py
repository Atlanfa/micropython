import pins
import states
from _thread import start_new_thread
from lab1 import blink_word
from lab2 import do_lab
from time import sleep


start_new_thread(blink_word, ("TESTING", ))
start_new_thread(do_lab, ("GPIO_PORT_ON_FOR_2S", pins.pin5, states.states, ))
sleep(10)
x