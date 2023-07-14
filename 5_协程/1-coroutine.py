"""
协程可以理解为微线程，由程序员调用，是在用户态执行的，比线程切换消耗的资源要少。对于异步非阻塞且还需要保留上下文的场景非常适用。
python可用yield实现协程，也可用第三方库主要有greenlet,stackless,gevent,eventlet等实现
"""

# from gevent import monkey
import gevent  # gevent使用 spawn 方法创建协程， joinall 方法启动协程。
import requests


def run_func(url):
    response = requests.get(url)
    print("%d bytes received from %s " % (len(response.content), url))


if __name__ == '__main__':
    urls = ['https://baidu.com/', 'https://www.python.org/', 'http://cnblogs.com/']
    greenlets = [gevent.spawn(run_func, _) for _ in urls]
    gevent.joinall(greenlets)



