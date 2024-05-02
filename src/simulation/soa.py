"""
Structure of arrays base class.
"""
# TODO: add division, difference
import numpy as np
import logging
logger = logging.getLogger("phoenix_simulation")


class StructureOfArrays:
    def __init__(self,
                 init_size: int,
                 state_size: int):
        self._init_size = init_size
        self._current_size = init_size
        self._state_size = state_size
        self._data = np.empty(shape=(self._init_size, self._state_size))
        self._end = 0

    def _increase_size(self):
        self._data = np.concatenate(
            (self._data, np.empty(shape=(self._current_size, self._state_size))),
            axis=0)
        self._current_size *= 2

    def add(self,
            state: np.ndarray):
        if self._end + 1 == self.current_size:
            self._increase_size()
        self._data[self._end, :] = state[:]
        self._end += 1

    def pop(self, index: int):
        # TODO:: add decrease of the size
        self._data[index, :] = state[self._end, : ]
        self._end -= 1

    def __add__(self, other: np.ndarray):
        return self._data[:self._end] + other

    def __iadd__(self, other: np.ndarray):
        return self._data[:self._end] + other

    def __mul__(self, other: np.ndarray):
        return self._data[:self._end] * other

    def __rmul__(self, other: np.ndarray):
        # NOTE: as much as possible we wish to not use this operator
        # python starts by calling mul on the left object, it will fail
        # in our case
        return other * self._data[:self._end]

    def __iadd_(self, other):
        self._data[:self.end] += other

    def __imul_(self, other):
        self._data[:self.end] *= other
