# Kafka producer for traffic sensor simulation
from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_traffic_data():
    return {
        "sensor_id": random.randint(1, 100),
        "timestamp": time.time(),
        "vehicle_count": random.randint(0, 200),
        "avg_speed_kmh": random.uniform(10, 120),
        "zone": random.choice(["north", "south", "east", "west"])
    }

if __name__ == "__main__":
    print("Starting traffic data producer...")
    while True:
        data = generate_traffic_data()
        producer.send('traffic-data', value=data)
        print(f"Sent: {data}")
        time.sleep(0.01)  # ~100 messages per second per producer
```

**Step 5** — Click **"Commit new file"** → **"Commit new file"**

Repeat this for the other two repos — paste any Python script you have for those projects, even partial code.

---

## Part 6 — Add your GitHub link to your resume

**Step 1** — Open your resume `.tex` file in Overleaf (paste it at overleaf.com)

**Step 2** — Find this line in the heading section:
```
\href{https://linkedin.com/in/darpanaryal-910a93176}{linkedin.com/in/darpanaryal}
```

**Step 3** — Add your GitHub right after it:
```
$|$ \href{https://github.com/darpanaryal}{github.com/darpanaryal}