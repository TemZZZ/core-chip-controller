import socket




class ControllerSocket:

    def __init__(self, host, port):

        self._sock = socket.socket()
        self._sock.connect( (host, port) )


    def __del__(self):
        self._sock.close()
