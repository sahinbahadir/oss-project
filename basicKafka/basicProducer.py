from time import sleep
from json import dumps
from kafka import KafkaProducer
import json
from flask import Flask, request


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

app = Flask(__name__)


@app.route('/', methods=['POST'])
def sendData():
    data = request.get_json()
    producer.send('topic_test', value=data)
    return data

if __name__ == '__main__':
    app.run(debug=True)