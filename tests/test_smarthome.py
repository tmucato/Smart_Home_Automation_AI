import unittest
from app.smarthome import SmartHome

class TestSmartHome(unittest.TestCase):
    def test_initialization(self):
        smarthome = SmartHome()
        self.assertIsNotNone(smarthome.light)
        self.assertIsNotNone(smarthome.fan)
        self.assertIsNotNone(smarthome.thermostat)

if __name__ == "__main__":
    unittest.main()