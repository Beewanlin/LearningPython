网络编程就是  本机进程 连接到 指定服务器进程 的端口进行通信（数据交换），所以网络编程的实质是进程通信。

Python的网络编程主要使用到两个模块：Socket模块 和 SocketServer模块。

网络通信的概念是Socket。
打开一个socket，即打开一个网络连接，需要知道目标主机的ip和端口号，并在通信时指定通信协议类型（TCP/UDP）。

新建一个socket需要按格式指定参数：socket(family, type, [,protocal])，这三个参数分别为 地址族、套接字类型、协议编号（默认为0 ）
例如：
创建 TCP socket：s = socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.SOCK_STREAM是流式套接字
创建 UDP socket：s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)，socket.SOCK_DGRAM是数据报套接字

socket函数：
服务端：
s.bind()
s.listen()
s.accept()
客户端：
s.connect()
公共：
s.recv()
s.send()
s.close()
s.settimeout(timeout)


TCP编程，服务端与客户端交流过程：
对于服务端：创建socket绑定指定ip和端口，监听指定端口，对每个新连接创建一个线程或进程来处理。
对于客户端：主动连接服务端，指定某个ip和端口；

UDP编程，服务端与客户端交流过程：
对于服务端：创建socket绑定指定ip和端口，直接发送或接收数据，最后关闭socket即可。
对于客户端：直接发送数据到指定端口；
注意：UDP与TCP的数据交流方式相似，但是UDP不需要建立连接，即 s.connect；此外，UDP和TCP的端口即使定为同一个也互不冲突。