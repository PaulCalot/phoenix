import logging

logger = logging.getLogger("visualization")


def visualize(msg, command):
    logger.info(f"Command: {command}, msg={msg}")
