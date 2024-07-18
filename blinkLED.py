from machine import Pin
import time

LED= Pin(25, Pin.OUT)
LED_EXT= Pin(26, Pin.OUT)

def main():
    
    while (True):
        LED.on()
        time.sleep(0.1)
        LED.off()
        time.sleep(0.1)
        LED_EXT.on()
        time.sleep(0.1)
        LED_EXT.off()
        time.sleep(0.1)
if __name__ == "__main__":
    main()