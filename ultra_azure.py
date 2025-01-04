from gpiozero import DistanceSensor
from azure.iot.device import IoTHubDeviceClient, Message
import time

# Azure IoT Hub connection string
CONNECTION_STRING = "YOUR CONNECTION STRING"

# Create the IoT Hub device client
device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

# Initialize the sensor on GPIO 23 and 24
sensor = DistanceSensor(echo=24, trigger=23)

print("Program started")

def send_data_to_iot_hub(distance):
    message = Message(f"{{'distance': {distance}}}")  # Create the telemetry message
    device_client.send_message(message)  # Send the message to Azure IoT Hub
    print(f"Sent message: {message}")

try:
    while True:
        dist = sensor.distance * 100  # Convert distance to centimeters
        print(f"Measured Distance: {dist:.2f} cm")

        # Send the measured distance to IoT Hub
        send_data_to_iot_hub(dist)
        
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")

finally:
    device_client.shutdown()  # Close the connection when done
