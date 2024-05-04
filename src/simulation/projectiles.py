from . import soa
import numpy as np
import logging

logger = logging.getLogger("phoenix_simulation")


class Projectiles:
    speed = 1000 # m/s
    life_span = 10 # s
    nb_projectiles = 100

    def __init__(self):
        # x, y, vx, vy
        logger.info(f"Creating bucket for {self.nb_projectiles} projectiles.")
        self._soa = soa.StructureOfArrays(self.nb_projectiles, 5)

    def fire(self,
             pos: (float, float),
             dir: (float, float)):
        vel = self.speed * dir / np.sqrt(dir[0]**2 + dir[1]**2)
        self._soa.add(np.array((pos[0], pos[1], vel[0], vel[1], 0.)))

    def update(self, dt: float):
        states = self._soa.get_states()
        states[:, 0:2] += dt * states[:, 2:4]
        states[:, 4] += dt
        self._soa.update_states(states)

        dead_projectiles = states[:, 4] > self.life_span
        for index, is_dead in enumerate(dead_projectiles):
            if(is_dead):
                self._soa.pop(index)
