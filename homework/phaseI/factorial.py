#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Python code to demonstrate math.factorial()
def factorial(number):
    import math
    print(f" {number} 的阶乘为: {math.factorial(number)}.")


# Python code to demonstrate naive method to compute factorial
def factorial_naive(number):
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
    print(f"{number} 的阶乘为: {fact}. ")


if __name__ == '__main__':
    number = int(input("请输入一个数字: "))
    if number < 0:
        print("抱歉，负数没有阶乘")
    elif number == 0:
        print("0 的阶乘为 1")
    else:
        factorial(number)
        factorial_naive(number)
