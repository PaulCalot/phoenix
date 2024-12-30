# TODO: what happens if multiple clients connect ?
import argparse
import socket
import logging
import time
from simulation import connection
import threading

simulation_state = {'value' : 0,
                    'fps': 1000}

def get_logging():
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("phoenix_simulation").setLevel(logging.INFO)

    logger = logging.getLogger()
    return logger


def run_simulation():
    while True:
        fps = 1000
        with threading.Lock():
            simulation_state['value'] += 1
            fps = simulation_state['fps']
        # TODO : now, the goal is to make the simulation as fast as possible
        # and if being observed, "add" some time so this amounst as much as possible to
        # the expected fps
        time.sleep(60 / fps)


def main(logger):
    # run simulation
    logger.info("Init the simulation...")
    simulation_thread = threading.Thread(target=run_simulation)
    simulation_thread.daemon = True
    simulation_thread.start()

    logger.info("Creating server socket...")
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(("localhost", 12345))
    serversocket.listen(5)

    count_connection = 0

    try:
        while 1:
            (clientsocket, address) = serversocket.accept()
            count_connection += 1
            with threading.Lock():
                simulation_state['fps'] = 60
            clientsocket.settimeout(10.0)
            client_socket = connection.SimulationSocket(clientsocket)
            try:
                while True:
                    with threading.Lock():
                        # TODO: should add some formatting function
                        msg = str(simulation_state['value'])
                    logger.info(f"Sending msg to {address}...")
                    client_socket.send("C", msg)
                    time.sleep(1)
            except BrokenPipeError:
                print("Detected broken pipe - client may have disconnected.")
            except ConnectionResetError:
                print("Connection reset by peer - client may have restarted or disconnected unexpectedly.")
            except socket.timeout:
                print("Socket operation timed out.")
            except socket.error as e:
                print(f"Socket error occurred: {e}") 
            finally:
                count_connection -= 1
                if (count_connection == 0):
                    with threading.Lock():
                        simulation_state['fps'] = 1000
    except KeyboardInterrupt:
        print("Simulation stopped by user.")
    finally:
        serversocket.shutdown(socket.SHUT_RDWR)
        serversocket.close()

if __name__ == '__main__':
    logger = get_logging()
    main(logger)
