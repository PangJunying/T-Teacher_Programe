#!/usr/bin/env python
# -*- coding: UTF-8 -*-

x = int(input("请输入一个十进制整数："))
base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A')+6)]
print(base)

# dec2bin
# 十进制 to 二进制: bin()
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])
        print(mid)
    return ''.join([str(x) for x in mid[::-1]])

if __name__ == '__main__':
    print(f"二进制转换十进制：{dec2bin(x)}")
