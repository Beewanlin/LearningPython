"""
greenlet是什么？
一个greenlet是一个独立的小微线程，相当于一个堆栈，栈底是初始功能，栈顶是当前greenlet暂停在代码段的位置；
greenlet之间可以相互切换，从原先的greenlet跳到其他greenlet执行，则原先的greenlet被挂起。
每个greenlet都有一个父greenlet，多个greenlet可能有共同的父greenlet，子greenlet栈空后，执行该父greenlet。

greenlet的工作切换：当当前代码段访问网络IO阻塞时，greenlet会切换到另一段没有被阻塞的代码段执行，直到原先的阻塞状态消失再自动转换到原先代码段继续执行。

gevent的本质还是greenlet在实现工作切换。
"""


