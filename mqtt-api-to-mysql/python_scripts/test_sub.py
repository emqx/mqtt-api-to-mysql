# coding: utf-8
# mqtt_subscriber.py
import paho.mqtt.client as mqtt


# MQTT回调函数
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    # 订阅主题
    client.subscribe("mqttx/simulate/temp-data/response/")


def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")


# MQTT客户端设置
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# 连接到MQTT代理
client.connect("127.0.0.1", 1883, 60)

# 阻塞调用，等待连接完成和消息到达
client.loop_forever()
