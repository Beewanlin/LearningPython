"""
fork一次创建两个进程，父进程和子进程，从以下例子可以看出该程序同时运行了2个进程
注意该方法不能用于windows
"""
import os

if __name__ == '__main__':
    pid = os.fork()
    print("current process is running, pid is ", os.getpid())
    if pid < 0:
        print("error in fork")
    elif pid == 0:
        print("This is a child process")
    else:
        print("This is a parent process, pid is", pid)