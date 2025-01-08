# pi5_azure_iot_hub
# 🚀 IoT: Connecting HC-SR04 Ultrasonic Sensor to Raspberry Pi 5 for Azure IoT Hub Integration

## Overview
![image](https://github.com/user-attachments/assets/199ef3c0-9d3d-4210-85ec-b9949bcc28af)

This project demonstrates an IoT edge experiment where an HC-SR04 Ultrasonic Sensor is connected to a Raspberry Pi 5 to stream real-time data to Azure IoT Hub. The focus is on seamless integration between edge devices and cloud platforms for efficient data management and analytics.

---

## Data Flow
Sensor 🥿 → Raspberry Pi 5 ⚡ → Python + gpiozero, Azure IoT SDK 💻 → Azure IoT Hub 🌟 → Cloud Analytics 📈

---

## Highlights
- **Hardware Setup:**
  - Raspberry Pi 5
  - HC-SR04 Ultrasonic Sensor
- **Software:**
  - Python
  - Libraries: `gpiozero` for sensor interfacing and Azure IoT SDK for cloud communication
- **Cloud Integration:**
  - Azure IoT Hub for data management, analytics, and automation

---

## Hardware Setup
1. Connect the **HC-SR04 Ultrasonic Sensor** to the GPIO pins on the Raspberry Pi 5:
   - **Trigger Pin**: GPIO 23
   - **Echo Pin**: GPIO 24
2. Power the sensor using the Raspberry Pi’s 5V and GND pins.

---

## Software Requirements
- Python 3.x
- Libraries:
  - `gpiozero`
  - `azure.iot.device`

Install required libraries using pip:
```bash
pip install gpiozero azure-iot-device
```

---

## Program
The Python program interfaces with the HC-SR04 sensor to measure distance and sends the data to Azure IoT Hub.

```python
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
```

---

## How It Works
1. **Sensor Interfacing:**
   - The `gpiozero` library is used to interact with the HC-SR04 sensor. It measures the distance in centimeters.
2. **Cloud Communication:**
   - The Azure IoT SDK enables secure communication between the Raspberry Pi 5 and Azure IoT Hub.
   - The measured distance is packaged as a telemetry message and sent to the IoT Hub.
3. **Data Management:**
   - The IoT Hub processes the incoming data, which can be visualized and analyzed in Azure cloud services.

---

## Monitor Data
Use the Azure CLI to monitor the data sent to the Azure IoT Hub. Run the following commands:

1. Add the Azure IoT extension if not already installed:
   ```bash
   az extension add --name azure-iot
   ```
2. Monitor events from your IoT device:
   ```bash
   az iot hub monitor-events --hub-name YourIotHubName --device-id YourDeviceId
   ```

Replace `YourIotHubName` with the name of your Azure IoT Hub and `YourDeviceId` with the ID of your IoT device.

---

## Output
- Real-time measurement of distance displayed on the terminal.
- Telemetry data sent to Azure IoT Hub.

Example output:
```
Program started
Measured Distance: 12.34 cm
Sent message: {'distance': 12.34}
Measured Distance: 15.67 cm
Sent message: {'distance': 15.67}
```

---



---

## License
This project is licensed under the MIT License. Feel free to use and adapt it for your needs!

