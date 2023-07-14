"""
greenlet是什么？
一个greenlet是一个独立的小微线程，相当于一个堆栈，栈底是初始功能，栈顶是当前greenlet暂停在代码段的位置；
greenlet之间可以相互切换，从原先的greenlet跳到其他greenlet执行，则原先的greenlet被挂起。
每个greenlet都有一个父greenlet，多个greenlet可能有共同的父greenlet，子greenlet栈空后，执行该父greenlet。

greenlet的工作切换：当当前代码段访问网络IO阻塞时，greenlet会切换到另一段没有被阻塞的代码段执行，直到原先的阻塞状态消失再自动转换到原先代码段继续执行。

gevent的本质还是greenlet在实现工作切换。gevent提供了pools对动态数量的greenlet进行并发管理，常用于大量IO及网络操作的场景。

特别地，在最开头的地方gevent.monkey.patch_all()，通过使用猴子补丁将标准库中的同步模块自动的转换成异步,即修改标准库里面大部分的阻塞式系统调用，包括socket、ssl、threading和
select等模块，而变为协作式运行。当协程（即 greenlet）阻塞时会自动切换。 """

from gevent import monkey

monkey.patch_all()

import urllib.request
from gevent.pool import Pool


def run_task(url):
    print("Visit --> %s" % url)
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        print('%d bytes have received from %s' % (len(data), url))
    except Exception as e:
        print(e)
    return 'url: %s --> finish' % url


if __name__ == '__main__':
    pool = Pool(2)
    urls = ['https://baidu.com.cn', 'https://www.sina.com.cn', 'https://www.apple.com']
    results = pool.map(run_task, urls)
    print(results)
