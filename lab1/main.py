from lab1 import blink_word
from machine import Pin

pin4 = Pin(4, Pin.IN, Pin.PULL_UP)      #настройка 4го пина, к которому подключена кнопка

while True:
    if not pin4.value():  # проверяем сигнал передающийся на пин, если 0 то разрешаем работу если 1 запрещаем
        blink_word('SOS')


