import unittest
from app.devices.light import Light

class TestLight(unittest.TestCase):
    def test_turn_on(self):
        light = Light()
        light.turn_on()
        self.assertTrue(light.is_on)

    def test_turn_off(self):
        light = Light()
        light.turn_on()
        light.turn_off()
        self.assertFalse(light.is_on)

    def test_status(self):
        light = Light()
        self.assertEqual(light.status(), "OFF")
        light.turn_on()
        self.assertEqual(light.status(), "ON")

if __name__ == "__main__":
    unittest.main()