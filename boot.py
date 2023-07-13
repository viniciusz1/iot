# Complete project details at https://RandomNerdTutorials.com

import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp

esp.osdebug(None)
import gc
gc.collect()

ssid = 'iotpsin'
password = 'psin2023'
mqtt_server = 'mqtt.tago.io'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = 'ESP32_DHT11'
topic_sub = b'notification'
topic_pub = b'hello'
tago_io_username = "Token"
tago_io_device_token = "b69b6a84-ff4c-4a28-9278-df570c335928"

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
