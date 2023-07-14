"""
读写文件的第一步 打开文件，最后一步 关闭文件。
    打开文件调用函数 open：
        1个必填参数：文件路径
        2个可选参数：读写模式mode：
                        r：只读
                        w：可写
                        a：追加
                        b：二进制模式（可与其他模式组合，例如rb、wb）
                        +：读/写模式（可与其他模式组合，例如r+）
                    缓冲区参数 buffering：
                        0：不使用缓冲区，即直接将数据写到硬盘上
                        1：使用缓冲，数据先写到内存里；需注意此方式下，只有使用 flush函数 或 close函数 才会将数据写到硬盘上
                        1以上数字：使用缓冲，数值表示使用的缓冲区大小
                        -1或任何负数：使用默认缓冲区的大小
    关闭文件调用函数 close：
        基本方法：f.close()关闭对文件的饮用
        但是当文件操作中发生了IO
        实现方法2：try-finally 代码块 + close()函数
        实现方法3：with

    读文件
    read() 函数，不带参数表示一次性读取到内存中，适用于较小的文件
    read(size) 可选参数 size 表明每次读取多少字节
    readline() 函数，每次读取一行返回，适用于较大的文本文件
    readlines() 函数，一次性读取所有 但是按行返回列表，适用于较大的文本文件

    写文件
    与读文件类似
    write() 函数，参数为要写入的内容

"""
import os

curr_dir = os.getcwd()  # 获取当前文件夹路径
filepath = curr_dir+'/testfile'  # 文件名带后缀可能会报错

with open(filepath, 'r') as f:
    content = f.read()
    print(content)