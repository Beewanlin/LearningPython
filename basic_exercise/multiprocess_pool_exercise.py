import os
import random
import time
from multiprocessing import Pool


def run_task(num):
    print('current process %s(PID=%s) is running' % (num, os.getpid()))
    time.sleep(random.random()*3)
    print('current process %s(PID=%s) stopped' % (num, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s started' % os.getpid())
    p = Pool(processes=3)
    iterations = 5
    for i in range(iterations):
        p.apply_async(func=run_task, args=(i,))
    print('waiting for all children processes finished')
    p.close()
    p.join()  # join()方法实现进程间的同步
    print('all children processes have finished')
    print('Parent process %s stopped' % os.getpid())

