from time import sleep


def do_lab(current_state, pin, states):
    print(current_state)
    if current_state == states[0]:
        pin.on()
        current_state = states[1]
        sleep(2)
    elif current_state == states[1]:
        pin.off()
        current_state = states[2]
        sleep(1)
    elif current_state == states[2]:
        pin.on()
        current_state = states[3]
        sleep(1)
    elif current_state == states[3]:
        pin.off()
        current_state = states[0]
        sleep(3)
    return current_state


