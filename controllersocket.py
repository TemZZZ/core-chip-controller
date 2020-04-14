#coding=utf-8


import socket

import struct


MSG_FORMAT = "!7B"
PHASE_STEP = 5.625
ATT_STEP = 0.5




class ControllerSocket:

    def __init__(self, host, port):

        self._sock = socket.socket()
        self._sock.connect( (host, port) )

        self._states = [0, 0, 0, 0, 1, 0, 63]

        self.send_states(self._states)


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

        self._states = states

        msg_struct = struct.pack(MSG_FORMAT, *states)

        self._sock.send( bytes(msg_struct) )


    def _one_node_state(self, state, byte_number):

        self._states[byte_number] = state

        self.send_states(self._states)


    def set_vd1(self, state):
        self._one_node_state(state, 0)


    def set_vd2(self, state):
        self._one_node_state(state, 1)


    def set_vd_mid(self, state):
        self._one_node_state(state, 2)


    def set_sw1(self, state):
        self._one_node_state(state, 3)


    def set_sw2(self, state):
        self._one_node_state(state, 4)


    def set_phase_shift_state(self, state):
        self._one_node_state(state, 5)


    def set_att_state(self, state):
        self._one_node_state(state, 6)
