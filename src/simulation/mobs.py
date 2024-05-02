from . import soa
import numpy as np
import logging
logger = logging.getLogger("phoenix_simulation")


class Mobs:
    max_speed = 10 # m/s
    acceleration = 1 # m/s-2
    nb_mobs = 100

    def __init__(self):
        # x, y, vx, vy
        logger.info(f"Creating {self.nb_mobs} mobs.")
        self._soa = soa.StructureOfArrays(self.nb_mobs, 4)
