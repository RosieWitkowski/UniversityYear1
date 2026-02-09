# Circuit board (alarm_circuit.png) created using https://academo.org/demos/logic-gate-simulator/

def alarm(keycard: bool, alarm_active: bool, door_open: bool, motion_detected: bool) -> bool:
    if keycard or not alarm_active:
        print("Alarm not triggered.")
        return False 
    if door_open or motion_detected:
        print("!! Alarm triggered !!")
        return True

print(alarm(False, False, True, True)) # Not trigger
print(alarm(False, True, True, False)) # Trigger
print(alarm(True, True, True, True)) # Not trigger
print(alarm(False, True, False, True)) # Trigger

