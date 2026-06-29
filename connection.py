import pika
import time

def create_connection():
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='localhost')
            )
            return connection
        except pika.exceptions.AMQPConnectionError:
            print("Retrying connection...")
            time.sleep(2)