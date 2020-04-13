import socket

import struct




class ControllerSocket:

    def __init__(self, host, port):

        self._sock = socket.socket()
        self._sock.connect( (host, port) )


    def __del__(self):
        self._sock.close()


    def send_states(self, states):

        msg_struct = struct.pack("!7B", *states)

        self._sock.send( bytes(msg_struct) )
