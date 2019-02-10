import paho.mqtt.client as mqtt


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.connect("192.168.43.165", 1883, 60)
mqttc.subscribe("#", 0)
mqttc.loop_forever()