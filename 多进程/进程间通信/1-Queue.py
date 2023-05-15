"""
case：在父进程中创建3个子进程，2个写1个读
队列是进程间通信的一种方式，python提供multiprocessing库中的Queue包实现多进程之间的通信。
还有一种方式是管道（Pipe）该方法只适用于2个进程间的通信
"""
import os
import time
import random
from multiprocessing import Process, Queue


def proc_write(queue, urls):
    print("Write Process "+str(os.getpid())+" is running")
    for url in urls:
        queue.put(url)
        print("Putting "+url+" to queue")
        # time.sleep(random.random()*3)


def proc_read(queue):
    print("Read Process "+str(os.getpid())+" is running")
    while True:  # 注意这里是死循环，在主程序内需用terminate终止该进程
        print("Reading "+queue.get(blocked=True, timeout=3000)+" from queue")


if __name__ == '__main__':
    # 父进程创建queue
    queue = Queue()
    # 创建子进程 writer1、writer2、reader
    writer1 = Process(target=proc_write, args=(queue, ["url1", "url2", "url3", "url4", "url5", "url6"]))
    writer2 = Process(target=proc_write, args=(queue, ["url7", "url8", "url9", "url10", "url11", "url12", "url13"]))
    reader = Process(target=proc_read, args=(queue,))
    # 启动写子进程：
    writer1.start()
    # 启动读子进程：
    reader.start()
    writer2.start()
    # 等待写子进程停止：
    writer1.join()
    writer2.join()
    # 将读子进程终止：
    reader.terminate()

