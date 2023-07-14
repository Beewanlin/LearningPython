import random
import threading
import time


def thread_run(urls):
    print('thread %s is running' % threading.current_thread().name)
    for url in urls:
        print('%s ------- %s' % (threading.current_thread().name, url))
        time.sleep(random.random())
    print('%s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    print('%s is running' % threading.currentThread().name)
    t1 = threading.Thread(target=thread_run, name='THREAD1', args=(['url1', 'url2'],))
    t2 = threading.Thread(target=thread_run, name='THREAD2', args=(['url3', 'url4'],))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('%s ended.' % threading.current_thread().name)
