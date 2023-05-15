"""
多进程，os模块中的fork方法可以实现，但一般使用multiprocessing模块的Process类来动态地创建多进程。
Process 参数为 待执行函数 和 函数参数；start()方法启动进程，join()方法进行进程间同步。
"""
from multiprocessing import Process
import time
import os
import random


def async_func(input_para):
    print("Process "+input_para+": pid "+str(os.getpid())+" is processing...")
    time.sleep(random.random() * 3)
    print("Process " + input_para + " end")


if __name__ == '__main__':
    for i in range(5):
        p = Process(target=async_func, args=(str(i),))
        p.start()
    p.join()  # join方法 实现进程间同步
