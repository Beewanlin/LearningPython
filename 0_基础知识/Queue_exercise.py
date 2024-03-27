import os, time, random
from multiprocessing import Process, Queue


def write_proc(q, urls):
    print('process %s is writing' % os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s into queue' % url)
        time.sleep(random.random())


def read_proc(q):
    print('process %s is reading' % os.getpid())
    while True:
        url = q.get()
        print('Get %s from queue' % url)
        time.sleep(random.random())


if __name__ == '__main__':
    q = Queue()
    proc_w1 = Process(target=write_proc, args=(q, ['url1', 'url2', 'url3'],))
    proc_w2 = Process(target=write_proc, args=(q, ['url4', 'url5', 'url6'],))
    proc_r1 = Process(target=read_proc, args=(q,))

    proc_w1.start()
    proc_w2.start()

    proc_r1.start()

    proc_w1.join()
    proc_w2.join()

    proc_r1.terminate()


