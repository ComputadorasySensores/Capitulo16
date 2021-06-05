import tm1637
import time
from machine import Pin
tm = tm1637.TM1637(clk=Pin(1), dio=Pin(0))

sensor_temperatura_interno = machine.ADC(4)
factor_conversion = 3.3 / (65535)

while True:
    tm.brightness(4)
    lectura = sensor_temperatura_interno.read_u16() * factor_conversion
    temperatura = 27 - (lectura - 0.706)/0.001721
    tm.temperature(int(temperatura))
    time.sleep(1)
