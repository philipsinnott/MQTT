import time, requests, random
import paho.mqtt.client as mqtt

# GLOBAL VARIABLES
ip = "broker.hivemq.com"
port = 1883
keepalive = 60
client_id =  "h20phisi@laptop"
sub_topic = "h20phisi/devices/node1/down"
pub_topic = "h20phisi/devices/node1/up"
pub_count = 1

# Maps rc's to their meaning
request_codes =\
{
    0: "Connection successful",
    1: "Connection refused - incorrect protocol version",
    2: "Connection refused - invalid client identifier",
    3: "Connection refused - server unavailable",
    4: "Connection refused - bad username or password",
    5: "Connection refused - not authorised 6-255: Currently unused."
}

def on_connect(client, userdata, flags, rc):
    if (rc == 0):
        print(f"[+] Successfully connected to {ip} on port {1883} as {client_id}.")
    else:
        print(f"[-] {request_codes.get(rc)}")
    # client.subscribe("#")
    # print("[INFO] Subscribed to topic # by default.")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f"[{msg.topic}]: {bytes.decode(msg.payload)}")
    pub(client)

# The callback for when a SUBACK is received from the server. (?)
def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Subscribed to {sub_topic}.")

def on_publish(client,userdata,result):
    global pub_count
    print(f"[{pub_count}] Publishing data to {pub_topic}...")
    pub_count += 1

# Initialize a client
def create_client(clientid, cleansession=True):
    return mqtt.Client(clientid, cleansession)

# Connect to a broker
def connect(client, ip, port, keepalive):
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_publish = on_publish
    client.connect(ip, port, keepalive)
    #client.subscribe(sub_topic)
    sub(client, sub_topic)
    #pub(client)
    client.loop_forever()

# Subscribe
def sub(client, topic):
    client.subscribe(topic)

# Publish
def pub(client):
    client.publish(pub_topic, f"[FROM: {client_id}]\n{gen_data()}")
    time.sleep(5)
    # for i in range(50):
    #     client.publish(pub_topic, "pub data sent from laptop")
    #     time.sleep(5)

def gen_data():
    url = "https://api.brightsky.dev/weather?lat=52&lon=7.6&date=2020-04-21"
    data = requests.get(url).json()
    r = random.randint(0, 20)
    return data["weather"][r]

def main():
    client = create_client(client_id)
    connect(client, ip, port, keepalive)
    #pub(client)
    #client.subscribe(sub_topic)

if __name__ == "__main__":
    main()