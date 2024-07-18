from machine import Pin, I2C

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)

print("I2C ADDRESS: " +hex(i2c.scan()[0]).upper())