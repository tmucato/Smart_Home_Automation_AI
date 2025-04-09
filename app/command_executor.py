# Command Execution
def execute_command(parsed_command, smarthome):
    if not parsed_command:
        return "Sorry, I couldn't understand that command."

    action = parsed_command.get("action")
    device = parsed_command.get("device")
    params = parsed_command.get("params")

    if device == "light":
        dev = smarthome.light
    elif device == "fan":
        dev = smarthome.fan
    elif device == "thermostat":
        dev = smarthome.thermostat
    else:
        return "Device not recognized."

    try:
        if action == "turn_on":
            if device not in ["light", "fan"]:
                return f"Cannot turn on the {device}."
            dev.turn_on()
            return f"The {device} is now ON."
        elif action == "turn_off":
            if device not in ["light", "fan"]:
                return f"Cannot turn off the {device}."
            dev.turn_off()
            return f"The {device} is now OFF."
        elif action == "set_speed":
            if device != "fan":
                return "Cannot set speed for this device."
            if params not in ["low", "medium", "high"]:
                return "Invalid speed value."
            dev.set_speed(params)
            return f"The fan speed is set to {params}."
        elif action == "set_temperature":
            if device != "thermostat":
                return "Cannot set temperature for this device."
            try:
                temp = int(params)
            except:
                return "Invalid temperature value."
            dev.set_temperature(temp)
            return f"The thermostat is set to {temp}°C."
        elif action == "get_status":
            if device == "thermostat":
                temp = dev.status()
                return f"The thermostat is set to {temp}°C."
            else:
                status = dev.status()
                return f"The {device} is {status}."
        else:
            return "Unknown action."
    except Exception as e:
        return f"Error executing command: {str(e)}"