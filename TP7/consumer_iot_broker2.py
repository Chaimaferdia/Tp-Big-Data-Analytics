from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'iot-sensors',
    bootstrap_servers='localhost:9093',  
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("Consumer connected to broker 2")
for message in consumer:
    print(f"Received: {message.value}")
