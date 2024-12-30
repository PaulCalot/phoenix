"""
Easier way: discrete representation.
Even though we may implement a logic behind it with stateitions that are not integers...
In the end we place them in cells...
Then we do :
- id : 0 - empty space
- id : 1 - bot or human
- id : 2 - mobs
- id : 3 - projectile
If a projectile comes in contact with a bot/human, then the bot/human loses 1 hp.
If a projectile comes in contact with a mob, then the mob dies.
If a mob comes in contact with a bot, then the mob dies and the bot loses 1 hp

Then we have something like this, the map is represented row-major, in a 1D array:
    [[0, 1, 0],
     [0, 3, 0],
     [2, 0, 2]]
Yields, at least when sending to the viz client :
    [0, 1, 0, 0, 3, 0, 2, 0, 2]

NOTE: here we sync the different state of the simulation, but this is not the place
to do it... is it ?
In the case where it is, it should return the new arrays, or the indexes
to delete and new pv.
"""
import numpy as np


class DiscreteSimulationState:
    def __init__(self, i_cells: int, j_cells: int) -> None:
        self.j_cells = j_cells
        self.i_cells = i_cells
        self.nb_cells = i_cells * j_cells
        self.sim_state = np.array(self.nb_cells)

    def update_states(self,
                      projectiles_state: np.ndarray,
                      mobs_state: np.ndarray,
                      bot_state: np.ndarray):
        # TODO: optimize it afterwards, may be this can be vectorized
        projectile_state_id = 3
        mob_state_id = 2
        bot_state_id = 1
        self.sim_state[:, :] = 0
        for i, state in enumerate(projectiles_state):
            x, y = state
            i, j = np.floor(x), np.floor(y)
            self.sim_state[i * self.j_cells + j] = projectile_state_id
        for i, state in enumerate(mobs_state):
            x, y, vx, vy, ax, ay, pv = state
            i, j = np.floor(x), np.floor(y)
            pos_xy = i * self.j_cells + j
            if (self.sim_state[pos_xy] == projectile_state_id):
                if pv == 1:
                    self.sim_state[pos_xy] = 0
                else:
                    # TODO: should decrease its pv by 1
                    self.sim_state[pos_xy] = mob_state_id
            else:
                self.sim_state[pos_xy] = mob_state_id
        x, y, vx, vy, ax, ay, pv = bot_state
        i, j = np.floor(x), np.floor(y)
        self.sim_state[i * self.j_cells + j] = 1
        pos_xy = i * self.j_cells + j
        if (self.sim_state[pos_xy] == projectile_state_id):
            if pv == 1:
                self.sim_state[pos_xy] = 0
            else:
                # TODO: should decrease its pv by 1
                self.sim_state[pos_xy] = bot_state_id
        else:
            self.sim_state[pos_xy] = bot_state_id
