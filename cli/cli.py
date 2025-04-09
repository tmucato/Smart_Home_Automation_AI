from ..app.smarthome import SmartHome
from ..app.parse_command import parse_command
from ..app.command_executor import execute_command

# CLI Interface
def main():
    smarthome = SmartHome()
    print("Smart Home Control System. Enter a command or 'exit' to quit.")
    while True:
        command = input("> ")
        if command.lower() == "exit":
            break
        parsed = parse_command(command)
        feedback = execute_command(parsed, smarthome)
        print(feedback)

if __name__ == "__main__":
    main()