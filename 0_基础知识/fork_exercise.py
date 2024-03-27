"""
3_多进程
"""

import os

if __name__ == '__main__':
    print('current process/parent process is %s' % os.getpid())
    pid = os.fork()
    # os.fork()方法比较特殊，调用一次，返回2次。返回可能是0，说明当前进程是子进程，子进程中返回永远是0；或者返回了进程ID，说明当前进程是父进程，返回的是子进程ID。
    if pid < 0:
        print('ERROR')
    elif pid == 0:
        print('current process is ChildProcess %s, its ParentProcess %s created me.' % (os.getpid(), os.getppid()))
    else:
        print('current process is ParentProcess %s, its ChildProcess is %s' % (os.getpid(), pid))
