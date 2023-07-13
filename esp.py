import network
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
wlan = network.WLAN(network.STA_IF) # cria a interface Wifi
wlan.active(True) # ativa a interface
from umqttsimple import MQTTClient

ssid = 'iotpsin'
password = 'psin2023'
mqtt_broker_ip = "mqtt.tago.io"
client_id = "ESP32_DHT11"  
tago_io_username = "Token"
tago_io_device_token = "b69b6a84-ff4c-4a28-9278-df570c335928"

def connectESP():
  def sub_cb(topic, msg):
    print((topic, msg))
    if topic == b'notification' and msg == b'received':
      print('ESP received hello message')

  def connect_and_subscribe():
    global client_id, mqtt_server, topic_sub
    client = MQTTClient(client_id, mqtt_broker_ip)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_sub)
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_broker_ip, topic_sub))
    return client

  def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()

  try:
    client = connect_and_subscribe()
  except OSError as e:
    restart_and_reconnect()

  while True:
    try:
      client.check_msg()
      if (time.time() - last_message) > message_interval:
        msg = b'Hello #%d' % counter
        client.publish(topic_pub, msg)
        last_message = time.time()
        counter += 1
    except OSError as e:
      restart_and_reconnect()

while True:
  if(wlan.isconnected()):
    print('Conexão realizada com sucesso!')
    connectESP()
  else:
    wlan.connect(ssid, password) 
    print('Conectando ao WIFI...')
    
    

  
  
  
