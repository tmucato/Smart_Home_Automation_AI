import os
import json
import traceback
from dotenv import load_dotenv
from google import genai

load_dotenv()

def parse_command(command):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("[Error] GOOGLE_API_KEY not found in environment variables.")
        return None
    try:
        client = genai.Client(api_key=api_key)
        system_prompt = '''
        You are a smart home command parser. Respond in JSON with the following keys: "action", "device", "params".
        Valid actions: turn_on, turn_off, set_speed, set_temperature, get_status.
        Valid devices: light, fan, thermostat.
        Params: 
            - For "set_speed": one of ["low", "medium", "high"]
            - For "set_temperature": a number (e.g., 22)
            - For other actions: null
        Example: {"action": "turn_on", "device": "light", "params": null}
        '''
        prompt = f"{system_prompt}\n\nCommand: {command}"
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[prompt]
        )
        generated_text = response.text.strip().strip('`').strip('json').strip()
        parsed = json.loads(generated_text)
        return parsed

    except Exception as e:
        print(f"[Error] Failed to parse command: {e}")
        traceback.print_exc()
        return None