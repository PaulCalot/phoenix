from . import soa
import numpy as np
import logging
logger = logging.getLogger("phoenix_simulation")


class Mobs:
    max_speed = 10 # m/s
    acceleration = 1 # m/s-2
    nb_mobs = 10

    def __init__(self):
        # x, y, vx, vy
        logger.info(f"Creating bucket for {self.nb_mobs} mobs.")
        self._soa = soa.StructureOfArrays(self.nb_mobs, 7)

    def add(self,
            pos: (float, float),
            vel: (float, float),
            acc: (float, float),
            pv: int):
        self._soa.add(np.array((pos[0], pos[1],
                                vel[0], vel[1],
                                acc[0], acc[1],
                                pv)))

    def update(self, dt: float):
        states = self._soa.get_states()
        # TODO: choose scheme to use
        states[:, 0:4] += dt * states[:, 2:6]
        self._soa.update_states(states)
