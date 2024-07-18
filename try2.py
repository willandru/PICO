from machine import Pin
import time

LED = Pin(25, Pin.OUT)

def blink_pattern():
    for _ in range(5):  # Blink the LED 5 times
        LED.on()
        time.sleep(0.5)  # Keep the LED on for 0.5 seconds
        LED.off()
        time.sleep(0.5)  # Turn off the LED for 0.5 seconds

# Run the blink pattern
blink_pattern()
