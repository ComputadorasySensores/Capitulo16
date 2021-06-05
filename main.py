import tm1637
import time
from machine import Pin
tm = tm1637.TM1637(clk=Pin(1), dio=Pin(0))
Boton = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)

a=0
b=0

tm.numbers(a,b)

while True:
    if Boton.value() == 1:
        while True:
            tm.numbers(a,b)
            b = b+1
            if b > 59:
                b = 0
                a = a+1
            time.sleep(1)
