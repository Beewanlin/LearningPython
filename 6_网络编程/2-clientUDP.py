# coding:utf-8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Hello', b'World']:
    s.sendto(data, ('127.0.0.1', 9999))
    print(s.recv(1024).decode('utd-8'))
s.close()