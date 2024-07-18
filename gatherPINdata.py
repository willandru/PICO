import machine

def get_pin_info(pin):
    pin_obj = machine.Pin(pin)
    return {
        "Pin Number": pin,
        "Direction": "IN" if pin_obj.IN() else "OUT",
        "Value": pin_obj.value(),
    }

def print_pin_info(pin_info):
    print("Pin Number:", pin_info["Pin Number"])
    print("Direction:", pin_info["Direction"])
    print("Value:", pin_info["Value"])
    print("-" * 20)

# Get and print information for each available pin
for pin_number in range(28):  # Assuming 28 is the maximum number of pins on your MicroPython board
    pin_info = get_pin_info(pin_number)
    print_pin_info(pin_info)
