import machine
import time
from ssd1306 import SSD1306_I2C

pix_res_x = 128  # SSD1306 horizontal resolution
pix_res_y = 64   # SSD1306 vertical resolution

i2c_dev = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16), freq=200000)  # Initialize I2C
oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)  # Initialize OLED display

adcpin = 4
sensor = machine.ADC(adcpin)

def ReadTemperature():
    adc_value = sensor.read_u16()
    volt = (3.3 / 65535) * adc_value
    temperature = 27 - (volt - 0.706) / 0.001721
    return round(temperature, 1)

while True:
    temperature = ReadTemperature()
    oled.fill(0)  # Clear the display
    oled.text("Temp: {:.1f} C".format(temperature), 0, 0)  # Display temperature on OLED
    oled.show()  # Update OLED display
    time.sleep(0.5)
    