import socket
import struct
import logging
logger = logging.getLogger("simulation")
VERSION = '1'
HEADER_LENGTH = 4
HEADER_FORMAT = "BBH"


class SimulationSocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, command, msg):
        version_byte = ord(VERSION)
        command_byte = ord(command)
        msg_length = len(msg)
        header = struct.pack(HEADER_FORMAT, version_byte, command_byte, msg_length)
        msg_with_header = header + msg.encode()
        totalsent = 0
        while totalsent < msg_length + HEADER_LENGTH:
            sent = self.sock.send(msg_with_header[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def receive(self):
        logger.warn("Receiving message is not implemented for "
                    "the simulation server.")
        pass

    def close(self):
        self.sock.close()
