import queue
import time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# 之前服务进程已经将队列暴露在网络，因此任务进程注册时只需要提供名称即可，与服务进程中的名称一致。
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')


server_addr = '127.0.0.1'
port = 8001
manager = QueueManager(address=(server_addr, port), authkey=b'qiye')
manager.connect()

# 从网络上获取Queue对象，进行本地化，与服务进程是同一个队列
task = manager.get_task_queue()
result = manager.get_result_queue()

# 从task队列取任务，并把结果放到result队列里
for i in range(11):
    try:
        n = task.get(timeout=1)  # 每隔1s后取出任务
        r = '%s * %s = %s' % (i, i, i*i)
        print('result is %s' % r)
        time.sleep(1)
        result.put(r)  # 将任务结果放到result队列
    except queue.Empty:
        print('task queue is empty')

print('work exited')







