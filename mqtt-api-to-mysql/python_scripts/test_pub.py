# send_mqtt_message.py
import requests


def send_mqtt_message(url, topic, payload_dict):
    # 注意：这里payload_dict是一个字典，而不是字符串
    data = {
        'topic': topic,
        'payload': payload_dict  # 这里payload_dict是字典，requests会将其转换为JSON
    }
    # 使用json=参数，requests会自动处理JSON的序列化和Content-Type的设置
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(response.text)


if __name__ == "__main__":
    url = 'http://127.0.0.1:5000/publish_mqtt'
    topic = 'mqttx/simulate/temp-data/response/'
    # 将payload更改为字典
    payload_dict = {"status": "off", "message": "Turn off the air conditioning"}
    send_mqtt_message(url, topic, payload_dict)
