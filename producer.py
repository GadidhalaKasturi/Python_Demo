import pika
from connection import create_connection

QUEUE = "demo_queue"

def send_message(message):
    connection = create_connection()
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE, durable=True)

    channel.basic_publish(
        exchange='',
        routing_key=QUEUE,
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )

    print(f"[Producer] Sent: {message}")
    connection.close()