import paho.mqtt.client as mqtt

broker_address="192.168.0.58"
port=1882
username="pratyay"
password="26324926"

def on_connect(client,userdata,flags,rc):
    print("Connected with result code "+str(rc))
    client.subscribe("pingpong")
    client.subscribe("mobile/text")

def on_message(client,userdata,msg):
    print("Message ["+msg.topic+"] : "+str(msg.payload))

client=mqtt.Client("p1")
client.connect(broker_address,port)
client.username_pw_set("pratyay","26324926")
client.on_connect=on_connect
client.on_message=on_message
client.loop_forever()



