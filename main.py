import argparse
import logging
from simulation import mobs

logger = logging.getLogger()
logging.getLogger("phoenix_simulation").setLevel(logging.INFO)


def main():
    _mobs = mobs.Mobs()


if __name__ == '__main__':
    main()
