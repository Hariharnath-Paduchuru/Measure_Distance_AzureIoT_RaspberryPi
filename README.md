# Measure Distance with RaspberryPi and Send to Azure IoT Hub
Measure Distance from Ultrasonic sensor by interfacing it with Raspberry Pi and Send to Azure IoT Hub

## Running the Python Code on Raspberry Pi

### Prerequisites
- Create [IoT Hub](https://youtu.be/dMa-gjzV-3M) and [IoT Hub Device](https://youtu.be/7kJom1CDaYs) in Azure. Follow the steps on Youtube if not created.

- Python 3: Raspberry Pi typically comes with Python pre-installed, but you can ensure you have Python 3 installed by running the following command in the terminal:

    ```
    python3 --version
    ```

    If it's not installed, you can install it by running:

    ```
    sudo apt update
    sudo apt install python3
    ```

### Step 1: Install the Required Packages

- Open a terminal on your Raspberry Pi.

- Run the following command to install the necessary packages:

    ```
    pip3 install azure-iot-device asyncio
    ```
    
### Step 2: Components required
- Raspberry Pi 3B (We can also use any other models of Pi)
- Micro SD Card-16 GB with Raspberry Pi OS
- Micro USB 5V, 2.4A Power supply
- HC-SR04 Module
- Resistors: 330Ω and 470Ω
- Jumper wires
- Breadboard

### Step 3: Hardware schematic

![Hardware Schematic](./ultrasonic_Raspberrypi.png)


### Step 4: Save the Code

- Create a new file on your Raspberry Pi and save the provided Python code into that file, for example, `measure_distance_AzureIoT_Pi.py`.

### Step 5: Obtain the Device Connection String

- Replace `<your_device_connection_string>` in the code with the actual connection string for your Azure IoT Hub device. You can find the connection string in the Azure portal under your IoT Hub's "Shared access policies" section.

### Step 6: Run the Code

- Open a terminal on your Raspberry Pi.

- Navigate to the directory where you saved the Python file.
- Before running the code, You should use the Azure IoT Explorer to monitor the data received at the IoT Hub.
- To configure the Azure IoT Explorer, look into the steps mentioned [here](https://github.com/Azure/azure-iot-explorer)
- Run the following command to start running the Python code:

    ```
    python3 measure_distance_AzureIoT_Pi.py
    ```

- The code will now start sending the measured Distance values to your Azure IoT Hub device. You should see the message being printed on the console as well.


That's it! You have successfully run the Python code on your Raspberry Pi to send the measured Distance values to your Azure IoT Hub device.

