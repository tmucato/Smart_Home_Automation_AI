import unittest
from app.devices.fan import Fan

class TestFan(unittest.TestCase):
    def test_turn_on(self):
        fan = Fan()
        fan.turn_on()
        self.assertTrue(fan.is_on)
        self.assertEqual(fan.speed, "low")

    def test_turn_off(self):
        fan = Fan()
        fan.turn_on()
        fan.turn_off()
        self.assertFalse(fan.is_on)
        self.assertEqual(fan.speed, "off")

    def test_set_speed(self):
        fan = Fan()
        fan.set_speed("medium")
        self.assertEqual(fan.speed, "medium")
        self.assertTrue(fan.is_on)

    def test_invalid_speed(self):
        fan = Fan()
        with self.assertRaises(ValueError):
            fan.set_speed("invalid")

    def test_status(self):
        fan = Fan()
        self.assertEqual(fan.status(), "OFF")
        fan.turn_on()
        self.assertEqual(fan.status(), "ON (speed: low)")

if __name__ == "__main__":
    unittest.main()