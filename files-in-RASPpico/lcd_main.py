import machine
import time
from machine import Pin, ADC
from esp32_gpio_lcd import GpioLcd

# Initialize ADC for reading internal temperature sensor
sensor = machine.ADC(4)

# Function to read temperature
def read_temperature():
    adc_value = sensor.read_u16()
    volt = (3.3 / 65535) * adc_value
    temperature = 27 - (volt - 0.706) / 0.001721
    return temperature

# Initialize LCD
lcd = GpioLcd(rs_pin=Pin(26),
              enable_pin=Pin(19),
              d4_pin=Pin(13),
              d5_pin=Pin(6),
              d6_pin=Pin(5),
              d7_pin=Pin(11),
              num_lines=2, num_columns=16)

# Main loop
while True:
    # Read temperature
    temperature = read_temperature()
    
    # Clear LCD
    lcd.clear()
    
    # Print temperature on LCD
    lcd.putstr('Temp:{:.1f} C'.format(temperature))
    
    # Wait for 1 second
    time.sleep(1)

