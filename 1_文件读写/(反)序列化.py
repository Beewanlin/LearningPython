"""
序列化指的是 将原本在内存中的对象转化为字符串str，使其可存入磁盘或通过网络传输到别的机器上，实现「程序状态」的保存与共享。
反序列化指的是 将文件中的字符串转化为python对象，关键是文件内容的格式标准。

注意：转化为2进制，因此序列化和反序列化时open文化应附上b模式。

python2中序列化主要使用 cPickle 和 Pickle 两个模块，前者由C编写效率高很多;
python3已经取代了cPickle，可使用 import _pickle as cPickle;

"""
import _pickle as cPickle
import os

d = dict(a=[1, 2, 3], b=[2, 3, 4], c=[3, 4, 5])
cwd = os.getcwd()
filename = cwd+'/testfile2.txt'
with open(filename, 'wb') as f1:
    cPickle.dump(d, file=f1)

with open(filename, 'rb') as f2:
    d2 = cPickle.load(f2)
    print(d2)
