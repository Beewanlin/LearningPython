"""
case：两个进程，一个从管道接收数据，一个发送数据给管道。
管道是进程间通信的另一种方式，
"""
from multiprocessing import Process, Pipe
import time
import os
import random


def proc_send(pipe, urls):
    for url in urls:
        print("Process %s is sending %s" % (os.getpid(), url))
        pipe.send(url)
        time.sleep(random.random())


def proc_recv(pipe):
    while True:
        print("Process %s is receiving %s" % (os.getpid(), pipe.recv()))
        time.sleep(random.random())


if __name__ == '__main__':
    pipe = Pipe()
    p1 = Process(target=proc_send, args=(pipe[0], ["url_" + str(_) for _ in range(5)]))
    p2 = Process(target=proc_recv, args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join(timeout=5)
    p2.join(timeout=5)
