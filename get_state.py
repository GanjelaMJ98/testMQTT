import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time as t

def get_information():
    publish.single("cmnd/sonoff/STATUS","0", hostname="192.168.43.165")
 
def device_status(msg):
	if msg.topic == "stat/sonoff/STATUS":
		message = eval(msg.payload.decode("utf-8"))
		print("\nDevice")
		print("Module: "	+ 	str(message['Status']['Module']))
		print("Topic: " 	+ 	str(message['Status']['Topic']))
		print("Power: " 	+ 	str(message['Status']['Power']))

def	wifi_status(msg):
	if msg.topic == "stat/sonoff/STATUS3":
		message = eval(msg.payload.decode("utf-8"))
		print("\nWiFi")
		print("Wifi: " 		+ 	str(message['StatusLOG']['SSId'][0]))
		print("Password: " 	+ 	str(message['StatusLOG']['SSId'][1]))

def network_status(msg):
	if msg.topic == "stat/sonoff/STATUS5":
		message = eval(msg.payload.decode("utf-8"))
		print("\nNetwork")
		print("Hostname: " 	+ 	str(message['StatusNET']['Hostname']))
		print("IP: " 		+ 	str(message['StatusNET']['IPAddress']))
		print("Gateway: " 	+ 	str(message['StatusNET']['Gateway']))
		print("Subnetmask: "+ 	str(message['StatusNET']['Subnetmask']))
		print("DNSServer: " +	str(message['StatusNET']['DNSServer']))
		print("Mac: " 		+ 	str(message['StatusNET']['Mac']))

def mqtt_status(msg):
	if msg.topic == "stat/sonoff/STATUS6":
		message = eval(msg.payload.decode("utf-8"))
		print("\nMQTT")
		print("MQTT host: " + 	str(message['StatusMQT']['MqttHost']))
		print("MQTT port: " + 	str(message['StatusMQT']['MqttPort']))
		
		

def on_message(mqttc, obj, msg):
    device_status(msg)
    wifi_status(msg)
    network_status(msg)
    mqtt_status(msg)



get_information()

mqttc = mqtt.Client()
mqttc.on_message = on_message


mqttc.connect("192.168.43.165", 1883, 60)
mqttc.subscribe("#", 0)
mqttc.loop_forever()


