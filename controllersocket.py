#coding=utf-8


import socket

import struct




class ControllerSocket:

    def __init__(self, host, port):

        self._sock = socket.socket()
        self._sock.connect( (host, port) )


    def __del__(self):
        self._sock.close()


    # ���������� ����������� ��������� ����������,
    # ������, ������������� � �����������.
    # states - ������ ��� ������, ��������� �� ���� ����� �����:
    # ��������� RX (VD1): ���./����., ��������� �������� (0, 1);
    # ��������� TX (VD2): ���./����., ��������� �������� (0, 1);
    # ��������� MID (VD MID): ���./����., ��������� �������� (0, 1);
    # ���� SW1: ����. A/����. B, ��������� �������� (0, 1);
    # ���� SW2: ����. A/����. B, ��������� �������� (0, 1);
    # ����� ��������� �������������: ��������� �������� �� 0 �� 63 � ����� 1;
    # ����� ��������� �����������: ��������� �������� �� 0 �� 63 � ����� 1.
    def send_states(self, states):

        msg_struct = struct.pack("!7B", *states)

        self._sock.send( bytes(msg_struct) )
