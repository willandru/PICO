import machine
import time



adcpin = 4
sensor = machine.ADC(adcpin)

def ReadTemperature():
    adc_value = sensor.read_u16()
    volt = (3.3 / 65535) * adc_value
    temperature = 27 - (volt - 0.706) / 0.001721
    return temperature

while True:
    temperature = ReadTemperature()
    print(temperature)
    time.sleep(0.5)
