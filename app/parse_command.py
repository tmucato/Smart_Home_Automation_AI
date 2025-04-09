import openai
import json
import os

# OpenAI Integration
def parse_command(command):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        return None

    system_message = '''
    You are a smart home command parser. Respond in JSON with keys: "action", "device", "params".
    Possible actions: turn_on, turn_off, set_speed, set_temperature, get_status.
    Devices: light, fan, thermostat.
    Params: For set_speed: low/medium/high. For set_temperature: number. Else: null.
    Example: {"action": "turn_on", "device": "light", "params": null}
    '''
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": command}
            ],
            temperature=0
        )
        response_text = response.choices[0].message.content
        parsed = json.loads(response_text)
        return parsed
    except:
        return None