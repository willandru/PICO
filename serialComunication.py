import os

# Define the serial port device
serial_port = 'COM5'  # Update this with your actual serial port

# Open the serial port in non-blocking mode
serial_fd = os.open(serial_port, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)

try:
    # Read from the serial port in a loop
    while True:
        try:
            # Attempt to read 1 byte from the serial port
            data = os.read(serial_fd, 1)
            if data:
                # Decode the byte and print it
                print("Received:", data.decode('utf-8'))
        except BlockingIOError:
            # If no data is available, ignore and continue
            pass
except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Close the serial port
    os.close(serial_fd)
