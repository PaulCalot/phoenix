import argparse
import socket
import logging
import time
from simulation import mobs
from simulation import projectiles
from simulation import connection
from random import random

def get_logging():
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("phoenix_simulation").setLevel(logging.INFO)

    logger = logging.getLogger()
    return logger

def some_simulation():
    return "Hello world"

def main(logger):
    # _mobs = mobs.Mobs()
    # _projectiles = projectiles.Projectiles()
    # _mobs.add(pos=(-1, 1), vel=(1, 0), acc=(0, 0.1))
    # _mobs.add(pos=(1, 1), vel=(5, 1), acc=(-1, -1))
    # _mobs.add(pos=(-1, -1), vel=(0, 0), acc=(3, 2))
    # _mobs.add(pos=(1, -1), vel=(0, 0), acc=(1, 0.1))
    # dt = 1
    # count = 0
    # while True:
    #     count += 1
    #     _mobs.update(dt)
    #     _projectiles.update(dt)
    #     # projectiles
    #     if(random() > 0.3):
    #         _projectiles.fire(pos=(random(), random()), dir=(random(), random()))
    #
    #     logger.info(f"[{count}] mobs: {_mobs._soa._end}, projectiles: {_projectiles._soa._end}")
    #     if(count > 100):
    #         break
    logger.info("Creating server socket...")
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(("localhost", 12345))
    serversocket.listen(5)

    try:
        while 1:
            (clientsocket, address) = serversocket.accept()
            client_socket = connection.SimulationSocket(clientsocket)
            # TODO: handle the case when the client closes the connection
            # so we send data once in a while...
            # ideally, the simulation would still run in the back, independently of the client
            # but I don't know how to do that... yet
            # may be it should be a separate process ???
            while True:
                data = some_simulation()
                logger.info("Sending msg...")
                client_socket.send("C", data)
                time.sleep(1)
    except KeyboardInterrupt:
        print("Simulation stopped by user.")
    finally:
        serversocket.close()

if __name__ == '__main__':
    logger = get_logging()
    main(logger)
