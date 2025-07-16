import os
import sys

import pika
import pyfiglet
from rich.console import Console

console = Console()


def callback(ch, method, properties, body):
    console.print(f"\n [x] Received: {body.decode()}", style="bold green")


def main():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        channel = connection.channel()

        channel.queue_declare(queue="hello")

        channel.basic_consume(
            queue="hello", on_message_callback=callback, auto_ack=True
        )
        custom_font = "slant"
        atual_version = "1.0.0"
        ascii_banner = pyfiglet.figlet_format(f"RabbitMQ Ex", font=custom_font)
        console.print(
            ascii_banner + f" versão: {atual_version} by @joellpaim\n",
            style="bold blue",
        )

        console.print(
            " [*] Waiting for messages. To exit press CTRL+C", style="bold green"
        )
        channel.start_consuming()
    except KeyboardInterrupt:
        console.print("\n [o] Interrupted", style="bold red")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
