#!/home/jalexander/anaconda3/bin/python3

import socket


def send_message(message_to_send,server_host,server_port):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as connection_to_server:
        connection_to_server.connect((server_host,server_port))
        connection_to_server.sendall( b'{}'.format(message_to_send) )
        data = connection_to_server.recv(1024)
