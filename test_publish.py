import paho.mqtt.publish as publish
import time as t

while(1):
    publish.single("mytopic","Hello LOLOLOLO", hostname="localhost")
    t.sleep(3)
