#!/usr/bin/env python
# -*- coding: UTF-8 -*-

### 一种实现
"""
[理解Python中的RingBuffer环形缓冲区_漫步量化-CSDN博客_python 环形缓冲区]
(https://blog.csdn.net/The_Time_Runner/article/details/106456174)
"""


class RingBuffer:
    def __init__(self, size):
        self.data = [None for i in range(size)]

    def append(self, x):
        self.data.pop(0)  # remove the last one which index = -1
        self.data.append(x)  # add at the index = -1

    def get(self):
        return self.data


buf = RingBuffer(1)
for i in range(10):
    buf.append(i)
    print(buf.get())

if __name__ == '__main__':
    pass
