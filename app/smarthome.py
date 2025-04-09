from .devices.devices import Light, Fan, Thermostat

# Smart Home System
class SmartHome:
    def __init__(self):
        self.light = Light()
        self.fan = Fan()
        self.thermostat = Thermostat()