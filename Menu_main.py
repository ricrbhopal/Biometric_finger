# main_menu.py
import time
from finger_module import get_fingerprint, enroll_finger, delete_finger, get_num, finger
import adafruit_fingerprint


# Main Menu
while True:
    print("----------------")
    if finger.read_templates() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to read templates")
    print("Fingerprint templates:", finger.templates)
    print("e) Enroll print")
    print("f) Find print")
    print("d) Delete print")
    print("----------------")
    c = input("> ")

    if c == "e":
        location = get_num()
        if enroll_finger(finger, location):
            print(f"Fingerprint at ID #{location} enrolled successfully!")
        else:
            print(f"Failed to enroll fingerprint at ID #{location}.")
    elif c == "f":
        if get_fingerprint(finger):
            print("Detected #", finger.finger_id, "with confidence", finger.confidence)
        else:
            print("Finger not found")
    elif c == "d":
        location = get_num()
        if delete_finger(finger, location):
            print(f"Fingerprint at ID #{location} deleted!")
        else:
            print(f"Failed to delete fingerprint at ID #{location}.")
