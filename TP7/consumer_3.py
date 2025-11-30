from kafka import KafkaConsumer
import json
from datetime import datetime

consumer = KafkaConsumer(
    'iot-sensors',
    bootstrap_servers='localhost:9094',  
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("Consumer connected to broker 3")
message_count = 0

try:
    for message in consumer:
        message_count += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{message_count}] {timestamp} - Received: {message.value}")
except KeyboardInterrupt:
    print("\nConsumer stopped by user.")
