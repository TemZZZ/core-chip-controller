#coding=utf-8


import socket

import struct




class ControllerSocket:

    def __init__(self, host, port):

        self._sock = socket.socket()
        self._sock.connect( (host, port) )


    def __del__(self):
        self._sock.close()


    # Отправляет контроллеру состояния усилителей,
    # ключей, фазовращателя и аттенюатора.
    # states - список или кортеж, состоящий из семи целых чисел:
    # усилитель RX (VD1): вкл./выкл., возможные значения (0, 1);
    # усилитель TX (VD2): вкл./выкл., возможные значения (0, 1);
    # усилитель MID (VD MID): вкл./выкл., возможные значения (0, 1);
    # ключ SW1: сост. A/сост. B, возможные значения (0, 1);
    # ключ SW2: сост. A/сост. B, возможные значения (0, 1);
    # номер состояния фазовращателя: возможные значения от 0 до 63 с шагом 1;
    # номер состояния аттенюатора: возможные значения от 0 до 63 с шагом 1.
    def send_states(self, states):

        msg_struct = struct.pack("!7B", *states)

        self._sock.send( bytes(msg_struct) )
