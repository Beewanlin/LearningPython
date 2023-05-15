import random
import threading
import time

"""
基于thread_exercise.py改写，继承threading.Thread重写run方法。简化 新建多个线程。
"""


class MyThread(threading.Thread):
    def __init__(self, name, urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print('thread %s is running' % threading.current_thread().name)
        for url in self.urls:
            print('%s ------- %s' % (threading.current_thread().name, url))
            time.sleep(random.random())
        print('%s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    print('%s is running' % threading.currentThread().name)
    t1 = MyThread(name='THREAD1', urls=['url1', 'url2'])
    t2 = MyThread(name='THREAD2', urls=['url3', 'url4'])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('%s ended.' % threading.current_thread().name)
