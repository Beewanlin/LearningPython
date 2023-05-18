"""
managers子模块封装了网络通信的细节，可以直接使用以实现分布式多进程
"""
import queue
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager

# 第一步：建立2个队列
# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()


# 第二步：把队列注册在网络上
class QueueManager(BaseManager):
    pass


def get_task_queue():
    return task_queue


def get_result_queue():
    return result_queue


def test():
    # 第二步：将队列注册到网络上
    QueueManager.register('get_task_queue', callable=get_task_queue)
    QueueManager.register('get_result_queue', callable=get_result_queue)

    # 第三步：绑定端口，初始化manager对象
    host = '127.0.0.1'
    port = 8001
    manager = QueueManager(address=(host, port), authkey=b'qiye')

    # 第四步：启动管理器，启动队列，监听通信
    manager.start()

    # 第五步：通过管理实例的方法获得通过网络访问的queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 第六步：添加任务
    for n in range(10):
        task.put(n)
        print('put task %s.' % n)
    # 第七步：取结果
    print('try get result.')
    for i in range(11):
        try:
            r = result.get(timeout=10)
            print('result is %s' % r)
        except queue.Empty:
            print('result queue is empty.')

    # 最后一定要关闭，不然会报错管道未关闭
    manager.shutdown()
    print('master exit.')


if __name__ == '__main__':
    freeze_support()
    print('Start!')
    test()