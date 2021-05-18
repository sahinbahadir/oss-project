from kafka import KafkaConsumer
from json import loads
from time import sleep

consumer = KafkaConsumer(
    'topic_test',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

for msg in consumer:
    msg_data = msg.value
    # Do whatever you want
    print(msg_data)
    sleep(1)