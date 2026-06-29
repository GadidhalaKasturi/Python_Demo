from connection import create_connection

QUEUE = "demo_queue"
RESPONSE_QUEUE = "response_queue"

def callback(ch, method, properties, body):
    message = body.decode()
    print(f"[Server] Received: {message}")

    processed = f"Processed: {message}"

    ch.basic_publish(
        exchange='',
        routing_key=RESPONSE_QUEUE,
        body=processed
    )

    print(f"[Server] Sent: {processed}")

def start_server():
    connection = create_connection()
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE, durable=True)
    channel.queue_declare(queue=RESPONSE_QUEUE, durable=True)

    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=callback,
        auto_ack=True
    )

    print("[Server] Waiting...")
    channel.start_consuming()

if __name__ == "__main__":
    start_server()