class Device():
    def __init__(self):
        self.__on = True
        self.__power = 0
    def togglePower(self, onOff):
        if onOff:
            self.__on = True 
            print("<CLICK> on")
        else:
            self.__on = False
            print("<CLICK> off")

    def getOnStatus(self):
        return self.__on
    
    # Abstract method: Doesn't do anything but serves as a template - all child classes must implement this method
    def operate():
        pass

class Light(Device):
    def __init__(self):
        super().__init__()

    def operate(self, level):
        if not self._Device__on:
            print("Device cannot be toggled while turned off.")
            return self._Device__power
        
        print(f"Lighting up by {level}%")
        changed = self._Device__power + level
        if changed >= 100:
             self._Device__power = 100
        elif changed < 0:
             self._Device__power = 0
        else:
            self._Device__power = changed
        return self._Device__power

class Thermostat(Device):
    def __init__(self, min, max):
        super().__init__()
        self.__min = min 
        self.__max = max

    def operate(self, level):
        if not self._Device__on:
            print("Device cannot be toggled while turned off.")
            return self._Device__power
        
        print(f"Adjusting temperature by {level} degrees")
        changed = self._Device__power + level
        if changed > self.__max:
             self._Device__power = self.__max
        elif changed < self.__min:
             self._Device__power = self.__min
        else:
            self._Device__power = changed
        return self._Device__power
    
class Room():
    def __init__(self, name: str, devices: list[Device]):
        self.__name = name 
        self.__devices = devices 

    def getRoom(self):
        return (self.__name, self.__devices)

class House():
    def __init__(self, rooms: list[Room]):
        self.__rooms = rooms
    
    def toggleAll(self, onOff):
        print("Toggling all devices")
        for room in self.__rooms:
            for device in room._Room__devices:
                device.togglePower(onOff)
    
    def getRooms(self):
        return self.__rooms 


rooms = [Room('Kitchen', [Thermostat(15, 30), Thermostat(-18, -20), Light()]), Room('Bedroom', [Light()]), Room('Bathroom', [Light()])]
house = House(rooms)

# --------  TOGGLE TEST ----------
house.toggleAll(True) # Turns all on 
house.toggleAll(False) # Turns all off
house.toggleAll(False) # Turns all off 
house.toggleAll(True) # Turns all on 

rooms = house.getRooms()
name, devices = rooms[0].getRoom()
print(name) # Prints Kitchen

devices[1].togglePower(False) # During loop, prints 'cannot be toggled while turned off'
for device in devices:
    print(device.getOnStatus()) # Prints True for all other devices
    device.operate(5) # Prints degrees for thermostat, percentage for light


"""
# Temperature test case   
temp = thermostat1.operate(29)
print(temp) # Print 29
temp = thermostat1.operate(5)
print(temp) # Print 30
temp = thermostat1.operate(-15)
print(temp) # Print 15
temp = thermostat1.operate(-10)
print(temp) # Print 15
    
# Lighting test case
power = light1.operate(5)
print(power) # Prints 5
power = light1.operate(5)
print(power) # Prints 10
power = light1.operate(150)
print(power) # Prints -100
power = light1.operate(-90)
print(power) # Prints 10
power = light1.operate(-100)
print(power) # Prints 0"""