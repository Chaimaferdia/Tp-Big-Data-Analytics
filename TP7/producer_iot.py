from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

sensors = ['Machine1', 'Machine2', 'Machine3']

try:
    while True:
        for sensor in sensors:
            data = {
                'sensor': sensor,
                'temperature': random.randint(70, 90),
                'humidity': random.randint(30, 50)
            }
            producer.send('iot-sensors', value=data)
            print(f"Sent: {data}")
        time.sleep(2) 
except KeyboardInterrupt:
    print("Producer stopped.")
