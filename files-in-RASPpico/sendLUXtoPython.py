import machine
import time

# Define the UART pins
uart = machine.UART(0, baudrate=9600)  # UART0, baud rate 9600

# Main loop
while True:
    # Send '1' over UART
    uart.write(b'1\n')
    
    time.sleep(1)  # Send '1' every 1 second
