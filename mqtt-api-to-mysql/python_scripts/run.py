import requests
from flask import Flask, jsonify, request
from connect import get_latest_temperature, get_db_connection
import json


connection = None
API_URL = 'http://127.0.0.1:18083/api/v5/publish'
USERNAME = 'ee26b0dd4af7e749'
PASSWORD = 'GGh8wD9CMmAH5WAUVbQ1GwMRm54vI87W9CUeNoZd2FJcD'
app = Flask(__name__)


@app.route('/api/temperature', methods=['GET'])
def get_latest_temperature_endpoint():
    """
    获取最新的温度数据
    """
    latest_temp = get_latest_temperature(connection)  # 调用数据库帮助模块中的函数
    return jsonify(
        {"timestamp": latest_temp['timestamp'], "temperature": latest_temp['temperature']}), 200


def publish_message(topic, payload):
    headers = {
        'Content-Type': 'application/json',
    }
    auth = (USERNAME, PASSWORD)
    data = {
        'topic': topic,
        'payload': payload,
        # 可能需要其他字段，根据API要求来
    }
    response = requests.post(API_URL, json=data, auth=auth, headers=headers)
    return response.json()


@app.route('/publish_mqtt', methods=['POST'])
def publish_mqtt():
    # 从请求中获取必要的数据
    topic = request.json.get('topic', 'mqttx/simulate/temp-data/response/')
    payload_dict = request.json.get('payload', {"status": "on"})
    payload = json.dumps(payload_dict)
    result = publish_message(topic, payload)
    return jsonify(result), 200


if __name__ == '__main__':
    connection = get_db_connection()
    app.run(debug=True)
