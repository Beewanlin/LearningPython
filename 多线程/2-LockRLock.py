"""
为避免多个线程对同一数据更改，需要用到线程锁，python提供threading对象的Lock和RLock方法实现简单的线程同步。
锁具有 acquire 和 release 方法，在acquire和release其中执行的代码是锁定时执行的。
注意多次调用acquire但不release的话，Lock会造成死锁，而RLock由于用了count变量计算acquire的次数 可以避免死锁。
"""
import threading

mylock = threading.RLock()
num = 0  # 共享变量


class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self) -> None:
        global num  # 若想在函数内部对函数外的变量进行操作，就需要在函数内部声明其为global
        while True:
            mylock.acquire()
            print("%s is locked, the global num is %s" % (threading.current_thread().name, num))
            if num >= 4:
                mylock.release()
                print("%s is released, the global num is %s……thread end" % (threading.current_thread().name, num))
                break
            num += 1
            mylock.release()
            print("%s is released, the global num is %s" % (threading.current_thread().name, num))


if __name__ == '__main__':
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    t1.start()
    t2.start()
