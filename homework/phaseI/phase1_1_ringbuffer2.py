#!/usr/bin/env python
# -*- coding: UTF-8 -*-

## Sébastien Keim 的代码, Kitty Pang 注释理解（2021/04/17
"""
[Implementing a Ring Buffer - Python Cookbook [Book]]
(https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s19.html)
"""


class RingBuffer:  # 定义一个ringbuffer的类
    """
    class that implements a not-yet-full buffer
    """

    def __init__(self,size_max):
        self.max = size_max
        self.data = []

    class __Full:    ### 不懂
        """
        class that implements a full buffer
        """
        def append(self, x):
            """append an element overwirting the oldest one."""
            self.data[self.cur] = x
            self.cur = (self.cur + 1) % self.max    # 取模，不懂为什么？

        def get(self):
            """return list of elements in correct order"""
            return self.data[self.cur:]+self.data[:self.cur]  # 判断读和写位置是否相同

    def append(self,x):
        """append an element at the end of the buffer"""
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            # Permanently change self's class from non-full to full'''
            self.__class__ = self.__Full

    def get(self):
        """Return a list of elements from the oldest to the newest"""
        return self.data

"""
sample usage 1， 类似模块 collections.deque()
"""
# x = RingBuffer(1000)
# import time
# tm1 = time.time()
# for i in range(int(1e6)):
#     x.append(i)
#
# print(x.get()[:10])
# tm2 = time.time()
# print ("{:.2f}seconds".format(tm2-tm1))


if __name__ == '__main__':
    # #x = RingBuffer(5)   # 定义5个buffer 空间，用class的定义
    # # x.append(1); x.append(2); x.append(3); x.append(4)  # ringbuffer read 1、2、3、4号，通过调用class 的append部分
    # print(x.__class__, x.get())
    # #x.append(5)   # 再写入第五号
    # print(x.__class__, x.get())  # buffer用满5个
    # #x.append(6)  # 继续写第六个数据
    # print(x.data, x.get())  # 写的buffer 6号覆盖了1号。调用的是类的get 实例
    # x.append(7); x.append(8); x.append(9); x.append(10)
    # print(x.data, x.get())

    x = RingBuffer(1)
    print(x.__class__, x.get())
    print(x.data, x.get())
    x.append(1)
    print(x.__class__, x.get())
    print(x.data, x.get())
    x.append(4)
    print(x.data, x.get())
    print(len(x.get()))
