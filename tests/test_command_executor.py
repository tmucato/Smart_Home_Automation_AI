import unittest
from app.smarthome import SmartHome
from app.command_executor import execute_command

class TestCommandExecutor(unittest.TestCase):
    def test_execute_turn_on_light(self):
        smarthome = SmartHome()
        command = {"action": "turn_on", "device": "light", "params": None}
        result = execute_command(command, smarthome)
        self.assertEqual(result, "The light is now ON.")
        self.assertTrue(smarthome.light.is_on)

    def test_execute_turn_off_light(self):
        smarthome = SmartHome()
        smarthome.light.turn_on()
        command = {"action": "turn_off", "device": "light", "params": None}
        result = execute_command(command, smarthome)
        self.assertEqual(result, "The light is now OFF.")
        self.assertFalse(smarthome.light.is_on)

    def test_execute_invalid_device(self):
        smarthome = SmartHome()
        command = {"action": "turn_on", "device": "invalid_device", "params": None}
        result = execute_command(command, smarthome)
        self.assertEqual(result, "Device not recognized.")

if __name__ == "__main__":
    unittest.main()