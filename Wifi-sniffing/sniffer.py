import os
import time
from playsound import playsound


# Function to check Wi-Fi connections
def check_wifi_connections():
    previous_devices = set()

    while True:
        # Get the list of connected devices
        output = os.popen("arp -a")
        lines = output.read().splitlines()

        current_devices = set()
        for line in lines:
            if "dynamic" in line.lower():
                device = line.split(" ")[1]
                current_devices.add(device)

        # Check for new connections
        new_devices = current_devices - previous_devices
        if new_devices:
            return new_devices

        previous_devices = current_devices.copy()
        time.sleep(1)

# Main function
def main():
    print("Monitoring for new Wi-Fi connections...")
    while True:
        new_devices = check_wifi_connections()
        if new_devices:
            playsound("point.wav")  # Replace with your alert sound file
            print("Default Wi-Fi connection(s) detected:")
            for device in new_devices:
                print(device)
            break  # Exit the loop after handling the connection event

# Run the main function
if __name__ == "__main__":
    main()
