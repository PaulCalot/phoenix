"""
This is the client socket, which will connect to the app to get information I believe.
When it asks to connect, it should be sent the data to display.

The simulation-server is a bit harder I believe to code as I am still unsure how to send back the data.

Anyway, the string message format is 
VCLLDDDDDDD....
So, 
1 byte for version
1 byte for command
2 bytes for length
N bytes for the data

With a given maximum length, I should not go beyond.
"""
import socket
import struct
import logging
logger = logging.getLogger("phenix_visualization")
VERSION = '1'
HEADER_FORMAT = 'BBH'
HEADER_LENGTH = 4


class VisualizationSocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, msg):
        logger.warn("Sending message is not implemented for "
                    "the visualisation client.")
        pass

    def receive(self):
        header = self.sock.recv(HEADER_LENGTH)
        if header == '':
            raise RuntimeError("socket connection broken")

        header_size = struct.calcsize(HEADER_FORMAT)
        if header_size != HEADER_LENGTH:
            raise RuntimeError("wrong header size")

        version, command, expected_length = struct.unpack(HEADER_FORMAT,
                                                          header)
        version = chr(version)
        logger.info(f"Version: {version}")
        command = chr(command)
        logger.info(f"Command: {command}")
        # expected_length = chr(expected_length) # should it be length
        logger.info(f"expected length: {expected_length}")

        if (version != VERSION):
            raise RuntimeError(f"Version mismatch: {version} vs. {VERSION}")

        msg = self.receive_fixed_length(expected_length)
        return (msg, command)

    def receive_fixed_length(self, msg_length: int) -> str:
        chunks = []
        bytes_recd = 0
        while bytes_recd < msg_length:
            chunk = self.sock.recv(min(msg_length - bytes_recd, 2048))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return ''.join([chunk.decode('utf-8') for chunk in chunks])

    def shutdown(self, how: int):
        self.sock.shutdown(how)

    def close(self):
        self.sock.close()
