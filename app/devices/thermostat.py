class Thermostat:
    def __init__(self):
        self.temperature = 22

    def set_temperature(self, temp):
        self.temperature = max(18, min(int(temp), 30))

    def status(self):
        return self.temperature