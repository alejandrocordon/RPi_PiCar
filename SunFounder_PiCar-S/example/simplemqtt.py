#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import time

# Create client instance and connect to localhost
client = mqtt.Client()
client.connect("hairdresser.cloudmqtt.com",18849,60)


# Publish message to topic/iopi and set pin 1 on bus 1 to on
client.publish("masteriot", "1,1");
time.sleep(2)

# Publish message to topic/iopi and set pin 1 on bus 1 to off
client.publish("topic/masteriot", "1,0");
time.sleep(2)
# Publish message to topic/iopi and set pin 1 on bus 2 to on
client.publish("topic/masteriot", "17,1");
time.sleep(2)
# Publish message to topic/iopi and set pin 1 on bus 2 to off
client.publish("topic/masteriot", "17,0");
client.disconnect();