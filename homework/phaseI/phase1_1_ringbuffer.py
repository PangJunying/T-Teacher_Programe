#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import collections
import time

d = collections.deque(maxlen=1000)     # deque：类似列表容器，实现了在两端快速添加(append)和弹出(pop)
tm1 = time.time()
for i in range(int(1e6)):  # 1e6表示1*10^6
    d.append(i)    # append(x)：添加i到右端

print(list(d)[:1])  # 列表切片取前1个，只接受一个 buffer
d.clear()
tm2 = time.time()
print ("{:.2f}seconds".format(tm2 - tm1))   # 格式化打印，保留小数点后两位



if __name__ == '__main__':
    pass
