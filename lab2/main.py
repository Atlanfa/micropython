from lab2 import do_lab
import pins
import states


current_state = "GPIO_PORT_ON_FOR_2S"

while True:
    current_state = do_lab(current_state, pins.pin5, states.states)
