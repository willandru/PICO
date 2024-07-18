from machine import Pin, I2C, ADC, temperature
from ssd1306 import SSD1306_I2C
import framebuf, sys, time

pix_res_x = 128  # SSD1306 horizontal resolution
pix_res_y = 64   # SSD1306 vertical resolution

i2c_dev = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)  # start I2C on I2C1 (GPIO 26/27)
i2c_addr = [hex(ii) for ii in i2c_dev.scan()]  # get I2C address in hex format
if not i2c_addr:
    print('No I2C Display Found')
    sys.exit()  # exit routine if no dev found
else:
    print("I2C Address      : {}".format(i2c_addr[0]))  # I2C device address
    print("I2C Configuration: {}".format(i2c_dev))  # print I2C params

oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)  # oled controller

oled.write_cmd(0xc0)  # flip display to place 0,0 at lower-left corner
adc = ADC(4)  # ADC channel 4 for temperature sensor

while True:
    oled.fill(0)  # clear the display
    temp_celsius = temperature()
    temp_text = "Temp: {:.2f} C".format(temp_celsius)
    oled.text(temp_text, 0, 0)  # display temperature
    oled.show()  # show the temperature on the OLED
    time.sleep(1)  # wait for a second before updating the temperature again
