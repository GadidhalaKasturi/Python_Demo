# Python\_Demo



\# RabbitMQ + Flask + Threading Demo



\## Overview

This project demonstrates:

\- REST API using Flask

\- RabbitMQ messaging (Producer/Consumer)

\- Multi-threaded requests

\- Pytest automation



\## Workflow

Client → API → RabbitMQ → Consumer → Processing



\## Setup



1\. Install dependencies:

pip install -r requirements.txt



2\. Start RabbitMQ:

rabbitmq-server



3\. Run Consumer:

python consumer.py



4\. Run API:

python api.py



5\. Send message:

Invoke-RestMethod -Method POST -Uri http://127.0.0.1:5000/send -Headers @{"Content-Type"="application/json"} -Body '{"message":"Hello"}'



6\. Run tests:

pytest -v



\## Features

\- Durable queues

\- Persistent messages

\- Thread-safe producer

\- Concurrent API testing

