import logging
import time
from visualization import connection


def get_logging():
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("phoenix_visualization").setLevel(logging.INFO)
    logger = logging.getLogger()
    return logger


# TODO: use what is necessary
def display_message(message):
    print("Received message:", message)

def main(logger):
    viz_socket = connection.VisualizationSocket()
    logger.info("Connecting to localhost")
    viz_socket.connect('localhost', 12345)

    try:
        while True:
            message = viz_socket.receive()
            logging.info(f"received msg: {message}")
            if message:
                display_message(message)
            else:
                break
    except KeyboardInterrupt:
        print("Visualization stopped by user.")
    finally:
        viz_socket.close()

if __name__ == "__main__":
    logger = get_logging()
    main(logger)
