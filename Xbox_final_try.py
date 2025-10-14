import evdev

# Find the event interface corresponding to your Xbox controller
device = evdev.InputDevice('/dev/input/event21')  # Replace 'X' with the appropriate number

max_scroll = [0,0,0,0]  # format: MAX [L_X, R_X, L_Y, R_Y]
min_scroll = [0,0,0,0]  # format: MIN [L_X, R_X, L_Y, R_Y]

print("Listening for key, trigger, D-pad, and thumbstick events...")

for event in device.read_loop():
    try:
        if event.type == evdev.ecodes.EV_KEY:
            key_event = evdev.categorize(event)
            if key_event.keystate == key_event.key_down:
                print("Key pressed: %s" % key_event.keycode)
        elif event.type == evdev.ecodes.EV_ABS:
            absevent = evdev.categorize(event)
            if absevent.event.code == evdev.ecodes.ABS_X:
                print("Left thumbstick X value: %d" % absevent.event.value)
                if absevent.event.value > max_scroll[0]:
                    max_scroll[0] = absevent.event.value
                if absevent.event.value < min_scroll[0]:
                    min_scroll[0] = absevent.event.value
            elif absevent.event.code == evdev.ecodes.ABS_Y:
                print("Left thumbstick Y value: %d" % absevent.event.value)
                if absevent.event.value > max_scroll[2]:
                    max_scroll[2] = absevent.event.value
                if absevent.event.value < min_scroll[2]:
                    min_scroll[2] = absevent.event.value
            elif absevent.event.code == evdev.ecodes.ABS_RX:
                print("Right thumbstick X value: %d" % absevent.event.value)
                if absevent.event.value > max_scroll[1]:
                    max_scroll[1] = absevent.event.value
                if absevent.event.value < min_scroll[1]:
                    min_scroll[1] = absevent.event.value
            elif absevent.event.code == evdev.ecodes.ABS_RY:
                print("Right thumbstick Y value: %d" % absevent.event.value)
                if absevent.event.value > max_scroll[3]:
                    max_scroll[3] = absevent.event.value
                if absevent.event.value < min_scroll[3]:
                    min_scroll[3] = absevent.event.value
        elif event.type == evdev.ecodes.EV_REL:
            revent = evdev.categorize(event)
            if revent.event.code == evdev.ecodes.REL_X:
                print("Scroll X value: %d" % revent.event.value)
            elif revent.event.code == evdev.ecodes.REL_Y:
                print("Scroll Y value: %d" % revent.event.value)
    except KeyboardInterrupt:
        print('\n Interrupted by the user!!\n')
        print(f'\n The max LEFT X scroll: {max_scroll[0]}')
        print(f'The max RIGHT X scroll: {max_scroll[1]}')
        print(f'\n The max LEFT Y scromin {max_scroll[2]}')
        print(f'The max RIGHT X scroll: {max_scroll[3]}')
        
        print(f'\n The min LEFT X scroll: {min_scroll[0]}')
        print(f'The min RIGHT X scroll: {min_scroll[1]}')
        print(f'\n The min LEFT Y scroll: {min_scroll[2]}')
        print(f'The min RIGHT X scroll: {min_scroll[3]}')
        
