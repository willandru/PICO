from machine import Pin, ADC
from time import sleep

potA = ADC(Pin(26))
potB = ADC(Pin(27))

while True:
    A=potA.read_u16()
    B=potB.read_u16()
    print(' SEN 1 ', B-A)
    sleep(1)