# MQTT prova

 
import paho.mqtt.client as mqtt
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("CAR #1/CO2")
    client.subscribe("CAR #1/COUNT")
 
 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("prova.org", 1883, 60)
client.loop_forever()
