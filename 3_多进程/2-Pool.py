"""
当需要对很多个进程进行同步时，Process类的手工操作就比较繁琐，此时可以使用multiprocessing模块的进程池类Pool来实现。
Pool默认提供内核数个进程供用户调用
"""
import time
import random
from multiprocessing import Pool
import os


# 同步函数
def async_func(input_para):
    print("Pool Object " + input_para + ": pid " + str(os.getpid()) + " is processing...")
    time.sleep(random.random() * 3)
    print("Pool Object " + input_para + " end")


if __name__ == '__main__':
    p = Pool(processes=3)  # 线程池容量为3，旧的任务结束后新的任务使用的仍是旧的进程（可以从pid看出）
    for i in range(8):
        p.apply_async(async_func, str(i))
    p.close()  # Pool要等所有子进程执行完毕，才会调用join()使主进程阻塞。因此需要先调用close()，不让新的process进入，再调用join()进行进程同步。
    p.join()  # 主进程阻塞，等待子进程的退出
