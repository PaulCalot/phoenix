from . import soa

class Projectiles:
    speed = 1000 # m/s
    def __init__(self):
        # x, y, vx, vy
        self._soa = soa.StructureOfArrays(100, 4)

    def fire(self,
             pos: (float, float),
             dir: (float, float)):
        vel = self.speed * dir / dir.norm()
        self._soa.add(np.array((pos[0], pos[1], vel[0], vel[1])))

    def move(self, dt: float):
        pass
