# MQTT
---
A simple program in Python that uses the [paho.mqtt library](https://pypi.org/project/paho-mqtt) to communicate between two nodes, a simulated "laptop" and "sensor". Currently, both nodes act as publisher and subscriber. The sensor subscribes to *h20phisi/devices/node1/up*, and publishes to *h20phisi/devices/node1/down*, whilst the laptop does vice versa. [HiveMQ](broker.hivemq.com) is being used as the broker. The data being sent is just sample weather data collected via the free [Bright Sky API](https://brightsky.dev/).

## Usage
---
```
git clone https://github.com/philipsinnott/MQTT.git
cd MQTT
py sensor.py
wt nt -d .
py laptop.py
```

## Example
---
**Laptop:**
![image](https://user-images.githubusercontent.com/56341190/227933807-6285120b-3127-470e-826e-13d2230bdbe9.png)


**Sensor:**
![image](https://user-images.githubusercontent.com/56341190/227933674-c485d26c-88ba-42a6-8fb1-237ef0b5c10b.png)
