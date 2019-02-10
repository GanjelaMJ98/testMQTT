import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import time as t
modules = []
information = dict()



def power(cmd):
	if(cmd == "ON" or cmd == "OFF"):
		publish.single("cmnd/sonoff/POWER",cmd, hostname="192.168.43.165")
	else:
		print("ERROR CMD")

def active_module(msg):
	if msg.topic == "stat/sonoff/RESULT":
		message = eval(msg.payload.decode("utf-8"))
		global modules
		for module in message.values():
			modules.append(module)
		'''
		print("\nModules")
		print("Module: "	+ 	str(message['Module']))
		'''
		


def device_status(msg):
	if msg.topic == "stat/sonoff/STATUS":
		message = eval(msg.payload.decode("utf-8"))
		global information
		for key,value in message['Status'].items():
			information.update({str(key):str(value)})
		'''
		print("\nDevice")
		print("Module: "	+ 	str(message['Status']['Module']))
		print("Topic: " 	+ 	str(message['Status']['Topic']))
		print("Power: " 	+ 	str(message['Status']['Power']))
		'''


def	wifi_status(msg):
	if msg.topic == "stat/sonoff/STATUS3":
		message = eval(msg.payload.decode("utf-8"))
		global information
		for key,value in message['StatusLOG'].items():
			information.update({str(key):str(value)})
		'''
		print("\nWiFi")
		print("Wifi: " 		+ 	str(message['StatusLOG']['SSId'][0]))
		print("Password: " 	+ 	str(message['StatusLOG']['SSId'][1]))
		'''


def network_status(msg):
	if msg.topic == "stat/sonoff/STATUS5":
		message = eval(msg.payload.decode("utf-8"))
		global information
		for key,value in message['StatusNET'].items():
			information.update({str(key):str(value)})
		'''
		print("\nNetwork")
		print("Hostname: " 	+ 	str(message['StatusNET']['Hostname']))
		print("IP: " 		+ 	str(message['StatusNET']['IPAddress']))
		print("Gateway: " 	+ 	str(message['StatusNET']['Gateway']))
		print("Subnetmask: "+ 	str(message['StatusNET']['Subnetmask']))
		print("DNSServer: " +	str(message['StatusNET']['DNSServer']))
		print("Mac: " 		+ 	str(message['StatusNET']['Mac']))
		'''


def mqtt_status(msg):
	if msg.topic == "stat/sonoff/STATUS6":
		message = eval(msg.payload.decode("utf-8"))
		global information
		for key,value in message['StatusMQT'].items():
			information.update({str(key):str(value)})
		'''
		print("\nMQTT")
		print("MQTT host: " + 	str(message['StatusMQT']['MqttHost']))
		print("MQTT port: " + 	str(message['StatusMQT']['MqttPort']))
		'''


def print_msg_info(client,userdata,message):
	print("%s : %s" % (message.topic, message.payload))


def on_message_information(mqttc, obj, msg):
    device_status(msg)
    wifi_status(msg)
    network_status(msg)
    mqtt_status(msg)

def on_message_module(mqttc, obj, msg):
	active_module(msg)

def get_information():
	global information
	information = dict()
	publish.single("cmnd/sonoff/STATUS","0", hostname="192.168.43.165")
    #subscribe.callback(on_message,"#",hostname = '192.168.43.165')
	mqttc = mqtt.Client()
	mqttc.on_message = on_message_information
	mqttc.connect("192.168.43.165", 1883, 60)
	mqttc.subscribe("#", 0)
	mqttc.loop_start()
	t.sleep(1)
	mqttc.loop_stop() #почитать

	return(information)

def get_active_modules():
	global modules
	modules.clear()
	publish.single("cmnd/sonoff/MODULE","0", hostname="192.168.43.165")
	mqttc = mqtt.Client()
	mqttc.on_message = on_message_module
	mqttc.connect("192.168.43.165", 1883, 60)
	mqttc.subscribe("stat/sonoff/RESULT", 0)
	mqttc.loop_start()
	t.sleep(1)
	mqttc.loop_stop()
	return(modules)



if __name__ == "__main__":
	get_information()

	mqttc = mqtt.Client()
	mqttc.on_message = on_message
	mqttc.connect("192.168.43.165", 1883, 60)
	mqttc.subscribe("#", 0)
	mqttc.loop_forever()
