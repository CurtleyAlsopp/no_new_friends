#!/home/jalexander/anaconda3/bin/python3

import socket
import tkinter

def send_message(message_to_send,server_host,server_port,output_messages):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as connection_to_server:
        print(message_to_send)
        connection_to_server.connect((server_host,server_port))
        connection_to_server.sendall(message_to_send.encode("utf-8"))
        data = connection_to_server.recv(1024)
        server_response = ("Server Response:", repr(data))
        output_messages.insert(END, server_response)
