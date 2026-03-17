# Real-Time Traffic Data Pipeline

> End-to-end streaming pipeline — Apache Kafka · Apache Spark · AWS EC2 · Spark MLlib

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=flat&logo=apachekafka&logoColor=white)
![Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=flat&logo=apachespark&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonaws&logoColor=white)

---

## Problem Statement

Urban traffic congestion causes billions of dollars in lost productivity annually. Traditional batch-processed traffic reports are too slow for real-time intervention. This project builds a streaming pipeline that ingests, processes, and predicts congestion in near real-time.

---

## Architecture

```
Traffic Sensors
      │
      ▼
Kafka Producers ──► Kafka Topics (partitioned by sensor zone)
                          │
                          ▼
              Spark Structured Streaming
                  │              │
                  ▼              ▼
           Data Cleaning    MLlib Model
           & Aggregation    (Congestion Prediction)
                  │              │
                  └──────┬───────┘
                         ▼
                   AWS EC2 Dashboard
                  (Sub-60s latency)
```

---

## Key Results

| Metric | Value |
|---|---|
| Throughput | 5,000+ messages / minute |
| Congestion prediction accuracy | 94% |
| Dashboard latency | < 60 seconds |
| Model | Spark MLlib Random Forest |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Message broker | Apache Kafka |
| Stream processing | Apache Spark Structured Streaming |
| ML | Spark MLlib (Random Forest Classifier) |
| Deployment | AWS EC2 |
| Language | Python 3.10+ |
| Monitoring | Custom dashboard |

---

## Project Structure

```
realtime-traffic-pipeline/
├── producers/
│   └── traffic_producer.py       # Kafka message producers simulating sensors
├── consumers/
│   └── spark_streaming.py        # Spark Structured Streaming consumer
├── ml/
│   ├── train_model.py            # MLlib model training
│   └── predict.py                # Real-time prediction integration
├── dashboard/
│   └── visualize.py              # Dashboard rendering
├── config/
│   └── kafka_config.py           # Kafka broker configuration
├── requirements.txt
└── README.md
```

---

## Setup & Run

```bash
# Clone the repo
git clone https://github.com/darpanaryal/realtime-traffic-pipeline.git
cd realtime-traffic-pipeline

# Install dependencies
pip install -r requirements.txt

# Start Kafka (requires Kafka running locally or on AWS)
# Start producer
python producers/traffic_producer.py

# Start Spark streaming consumer
spark-submit consumers/spark_streaming.py
```

---

## What I Learned

- Designing fault-tolerant Kafka topic partitioning strategies for high-throughput ingestion
- Integrating Spark MLlib models directly into Structured Streaming pipelines
- Managing exactly-once semantics and offset checkpointing in production streaming
- Deploying distributed Spark jobs on AWS EC2 clusters

---

## Author

**Darpan Aryal** · [LinkedIn](https://linkedin.com/in/darpanaryal) · [aryaldarpan20@gmail.com](mailto:aryaldarpan20@gmail.com)
