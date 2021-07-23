import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("HMI")
client.connect(mqttBroker)

i = 0


def publish(msg):
    client.publish("Commands", msg)
    print("Команда '" + msg + "' передана")
    time.sleep(0.1)

def num():
    global i
    i += 1
    client.publish("Commands", i)