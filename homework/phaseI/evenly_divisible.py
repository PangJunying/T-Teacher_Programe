#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
实现 evenly_divisible() 函数，接受三个整数输入 a, b, c ，
要求输出在 [a, b] 范围内所有能够 被 c 整除的数之和，
比如 evenly_divisible(1, 10, 2) -> 30
"""

def evenly_divisible(num1, num2, num3):
    sum = 0
    if num1 > num2:
        num1, num2 = num2, num1
    else:
        pass

    for i in range(num1, num2+1):
        if i % num3 == 0:
            sum = i + sum
            i += 1
        else:
            continue
    return sum

if __name__ == '__main__':
    """
    缺exception 输入错误和负数的情况
    """
    a = int(input("请输入第一个正整字:"))
    b = int(input("请输入第二个正整字:"))
    c = int(input("请输入第三个正整字:"))

    print(f"数字{a}到数字{b}之间能被数字{c}整除的和为：{evenly_divisible(a,b,c)}")
