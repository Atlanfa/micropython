from lab1 import blink_word
import pins


while True:
    if not pins.pin4.value():  # проверяем сигнал передающийся на пин, если 0 то разрешаем работу если 1 запрещаем
        blink_word('SOS')


