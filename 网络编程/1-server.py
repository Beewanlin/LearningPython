"""
listen(n)：n表示的是服务器拒绝(超过限制数量的)连接之前，操作系统可以挂起的最大连接数量。n也可以看作是"排队的数量"。
排队的人数(就是那个n) + 正在就餐的人数（服务器正在处理的socket连接数) = 允许接待的总人数（socket允许的最大连接数）

sock具有2个方法，分别为send和recv。send参数为要发送的字符串，recv参数指的是接收的最大字节数（一般设置为1024，因为以太网的MTU为1500，不能设置的过大）
所以recv时需要循环接收缓冲区的消息并拼接。
"""

import socket
import threading
import time


def dealClient(sock, addr):
    # 第四步，接收传来的数据并发送数据给对方
    print('Accept new connection from %s' % addr)
    sock.send('I am a Server')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        print("-->>%s!" % data.decode('utf-8'))
        sock.send(('Loop_Msg: %s!' % data.decode('utf-8')).encode('utf-8'))
    # 第五步，关闭socket
    sock.close()
    print('Connection from %s: %s closed' % addr)





if __name__ == '__main__':
    # 第一步，建立socket 并绑定ip与端口
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind('127.0.0.1', 9999)
    # 第二步，开启监听，总共允许n+1个socket连接。listen(n)。
    s.listen(5)
    print('waiting for connection')
    while 1:
        # 第三步，接受一个新连接，并创建新线程来处理TCP连接
        sock, addr = s.accept()
        t = threading.Thread(target=dealClient, args=(sock, addr))
        t.start()

