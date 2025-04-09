import unittest
from app.devices.thermostat import Thermostat

class TestThermostat(unittest.TestCase):
    def test_set_temperature(self):
        thermostat = Thermostat()
        thermostat.set_temperature(25)
        self.assertEqual(thermostat.temperature, 25)

    def test_temperature_bounds(self):
        thermostat = Thermostat()
        thermostat.set_temperature(10)
        self.assertEqual(thermostat.temperature, 18)
        thermostat.set_temperature(35)
        self.assertEqual(thermostat.temperature, 30)

    def test_status(self):
        thermostat = Thermostat()
        self.assertEqual(thermostat.status(), 22)

if __name__ == "__main__":
    unittest.main()