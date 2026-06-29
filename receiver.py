from connection import create_connection

RESPONSE_QUEUE = "response_queue"

def callback(ch, method, properties, body):
    print(f"[Receiver] Got: {body.decode()}")

def start_receiver():
    connection = create_connection()
    channel = connection.channel()

    channel.queue_declare(queue=RESPONSE_QUEUE, durable=True)

    channel.basic_consume(
        queue=RESPONSE_QUEUE,
        on_message_callback=callback,
        auto_ack=True
    )

    print("[Receiver] Waiting...")
    channel.start_consuming()

if __name__ == "__main__":
    start_receiver()