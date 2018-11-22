# testMQTT

MQTT broker: Mosquitto
______________________
sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients

mosquitto_sub -d -h localhost -t mytopic

Python Client: Paho
______________________
pip install paho-mqtt

or

git clone https://github.com/eclipse/paho.mqtt.python.git
cd paho.mqtt.python
python setup.py install


https://habr.com/company/intel/blog/302338/
