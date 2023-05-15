"""
Python中由于CLI锁的存在，多进程里一个进程只能执行一个线程，因此即使是多核CPU，python的多线程也并不能被实现。
两种实现方式：1）创建threading.Thread类实例，传参 target,name,args；再用start启动线程；
2）继承threading.Thread类，重写threading.Thread类的init方法和run方法
"""
import random
import threading

# # 方式1
# def thread_run(input_para):
#     print("%s is running" % threading.current_thread().name)
#     for para in input_para:
#         print("%s ------> %s" % (threading.current_thread().name, para))
#     print("%s ended\n" % threading.current_thread().name)
#
#
# if __name__ == '__main__':
#     print("%s is running\n" % threading.current_thread().name)
#     t1 = threading.Thread(target=thread_run, name="Thread1", args=(["url1", "url2", "url3"],))
#     t2 = threading.Thread(target=thread_run, name='Thread2', args=(["url4", "url5", "url6"],))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print("%s ended\n" % threading.current_thread().name)

# 方式2：
import time


# 第二种实现方式
class MyThread(threading.Thread):
    def __init__(self, name, input_para):
        # self.name = name
        threading.Thread.__init__(self, name=name)
        self.args = input_para

    def run(self) -> None:
        print("%s is running\n" % threading.current_thread().name)
        for para in self.args:
            print("%s -------> %s" % (threading.current_thread().name, para))
            # time.sleep(random.random())
        print("%s ended" % threading.current_thread().name)


if __name__ == '__main__':
    t1 = MyThread(name="t1", input_para=["url1", "url2", "url3"])
    t2 = MyThread(name="t2", input_para=["url4", "url5", "url6"])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
