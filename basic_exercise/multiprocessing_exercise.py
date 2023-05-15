import os
import time
import random
from multiprocessing import Process


def run_proc(num):
    print('children process %s started' % os.getpid())
    print('No.%s child process %s is current process' % (num, os.getpid()))
    print('childprocess %s stopped' % os.getpid())


if __name__ == '__main__':
    iterations = 5
    print('Parent process %s started' % os.getpid())
    for i in range(iterations):
        p = Process(target=run_proc, args=(str(i+1),))
        p.start()
    p.join()  # join()方法实现进程间的同步
    print('Parent process %s stopped' % os.getpid())

"""
为什么 "args = (thread_number,)" 用逗号结尾？
【问题讨论】：
逗号定义了args期望的元组。
那么即使我们只有一个变量，这也需要吗？
是的，因为(x) 不是元组，而(x,) 是。除了空元组()，元组总是由逗号定义，而不是由括号定义。括号仅在此处用于消除元组逗号与虚构参数列表逗号的歧义。
"""



"""

"""