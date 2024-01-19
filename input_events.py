from evdev import InputDevice, categorize, ecodes

def print_events(device):
    print(f"Reading events from {device.name} (phys: {device.phys}, uniq: {device.uniq})")
    
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            print(f"Key event - Code: {key_event.event.code}, Type: {key_event.event.type}, Value: {key_event.event.value}")

# Replace '/dev/input/event24' and '/dev/input/event25' with the actual device paths
mouse_device = InputDevice('/dev/input/event24')
keyboard_device = InputDevice('/dev/input/event25')

# Print events for both devices
print_events(keyboard_device)
print_events(mouse_device)
