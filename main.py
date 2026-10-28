
import platform
import socket
import time
import os

class EC2Instance:
    def __init__(self, instance_id):
        self.instance_id = instance_id
        self.status = "Running"

    def execute_command(self, command):
        print(f"\nInstance: {self.instance_id}")
        print(f"Command: {command}")

        if command == "hostname":
            result = socket.gethostname()
        elif command == "date":
            result = time.strftime("%Y-%m-%d %H:%M:%S")
        elif command == "whoami":
            result = "ec2-user (simulation)"
        elif command == "os":
            result = platform.system()
        elif command == "pwd":
            result = os.getcwd()
        else:
            result = "Command simulated successfully"

        print("Status: Success")
        print("Output:", result)


print("AWS Systems Manager - Run Command Demo")

instance = EC2Instance("i-1234567890abcdef0")
print("Instance status:", instance.status)

commands = ["hostname", "date", "whoami", "os", "pwd"]

for command in commands:
    instance.execute_command(command)
