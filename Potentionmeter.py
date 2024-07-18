from machine import ADC
from time import sleep

def ReadPotentiometer():
    adcpin = 26
    pot = ADC(adcpin)
    
    adc_value = pot.read_u16()
    volt = (3.3/65535)*adc_value
    
    percentPot = ScalePercent(volt)
    
    return percentPot

def ScalePercent(volt):
    percent = (volt/3.3)*100
    return int(percent)

while True:
    potvalue = ReadPotentiometer()
    print(potvalue)
    sleep(1)