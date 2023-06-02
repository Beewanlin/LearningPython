import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 1.连接目标IP及端口
s.connect('127.0.0.1', 9999)
# 2.接收消息
print('——>'+s.recv(1024).decode('utf-8'))
# 3.发送消息
s.send(b'Hello, I am a client.')
print('——>'+s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
