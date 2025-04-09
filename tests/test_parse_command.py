import unittest
from app.parse_command import parse_command

class TestParseCommand(unittest.TestCase):
    def test_parse_valid_command(self):
        # Mock OpenAI API key in the environment
        import os
        os.environ["OPENAI_API_KEY"] = "test_key"

        # Mock OpenAI response (you'll need to mock the API call in real tests)
        command = "Turn on the light"
        result = parse_command(command)
        self.assertIsNotNone(result)

    def test_parse_invalid_command(self):
        command = ""
        result = parse_command(command)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()