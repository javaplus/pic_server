import paho.mqtt.client as mqtt
import logging
import file_uploader
import datetime

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("picture/pics")



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    #get message as bytearray and send it to a service?
    # maybe dump it to a file first to test
    data = msg.payload
    print("Got something something")
    fileName = getPictureName() 
    file_uploader.uploadFileToS3(data, 'test.jpg')

def getPictureName():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + ".jpg"

client = mqtt.Client("PicServer")
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
#client.connect("10.0.0.1", 1883, 60)
#client.connect("192.168.1.124", 1883, 60)
print("Doing Stuff")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
