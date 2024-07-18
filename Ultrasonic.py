import machine
import utime

# Define GPIO pins
TRIG_PIN = 14
ECHO_PIN = 15

# Initialize GPIO pins
trig = machine.Pin(TRIG_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)

# Function to measure distance
def measure_distance():
    # Send a 10us pulse to trigger the sensor
    trig.high()
    utime.sleep_us(10)
    trig.low()

    # Wait for the echo signal to go high
    while echo.value() == 0:
        pulse_start = utime.ticks_us()

    # Wait for the echo signal to go low
    while echo.value() == 1:
        pulse_end = utime.ticks_us()

    # Calculate duration of pulse
    pulse_duration = pulse_end - pulse_start

    # Speed of sound is approximately 343m/s
    # Dividing by 2 accounts for round trip
    distance = (pulse_duration * 343) / 2 / 10000  # Convert to centimeters
    return distance

# Main loop
while True:
    distance = measure_distance()
    print("Distance:", distance, "cm")
    utime.sleep(1)  # Delay between measurements
