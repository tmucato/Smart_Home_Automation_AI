class Fan:
    def __init__(self):
        self.is_on = False
        self.speed = "off"

    def turn_on(self):
        self.is_on = True
        if self.speed == "off":
            self.speed = "low"

    def turn_off(self):
        self.is_on = False
        self.speed = "off"

    def set_speed(self, speed):
        valid_speeds = ["low", "medium", "high"]
        if speed in valid_speeds:
            self.speed = speed
            self.is_on = True
        else:
            raise ValueError("Invalid speed. Choose low, medium, or high.")

    def status(self):
        if self.is_on:
            return f"ON (speed: {self.speed})"
        else:
            return "OFF"