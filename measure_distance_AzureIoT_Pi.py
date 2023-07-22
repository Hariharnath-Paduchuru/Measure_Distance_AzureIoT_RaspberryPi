# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
import asyncio
import time
import uuid
import sys
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message
import RPi.GPIO as GPIO
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

async def measure_distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

async def send_recurring_telemetry(device_client):
    # Connect the client.
    await device_client.connect()

    # Send recurring telemetry
    while True:
        distance = await measure_distance()
        msg_txt_formatted = '{{"distance": {distance}}}'
        data = msg_txt_formatted.format(distance=distance)
        msg = Message(data)
        msg.content_encoding = "utf-8"
        msg.content_type = "application/json"
        print("sending message - " + str(data))
        await device_client.send_message(msg)
        time.sleep(3)


def main():
    # The connection string for a device should never be stored in code. For the sake of simplicity we're using an environment variable here.
    conn_str = "<your_device_connection_string>"
    # The client object is used to interact with your Azure IoT hub.
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    print("IoTHub Device Client Recurring Telemetry Sample")
    print("Press Ctrl+C to exit")
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(send_recurring_telemetry(device_client))
    except KeyboardInterrupt:
        print("User initiated exit")
    except Exception:
        print("Unexpected exception!")
        raise
    finally:
        loop.run_until_complete(device_client.shutdown())
        loop.close()


if __name__ == "__main__":
    main()
