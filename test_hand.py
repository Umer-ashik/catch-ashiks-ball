from hand_tracker import get_finger_position

try:
    while True:
        position = get_finger_position()
        print(position)
except KeyboardInterrupt:
    print("\nstopping the hand tracker...")