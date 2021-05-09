#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 实现 string_pairs() 函数，接受一个字符串输入，输出一个成对字符的列表，
# 如果不是偶数位， 则使用 * 补足，比如 string_pairs('hello') -> ['he', 'll', 'o*']



def string_pairs(the_string):

    l = "".join(the_string) # 将列表变成字符串
    list1 = []
    str1 = ""
    addition_number = 0  # 设置开始读的变量
    i = 1
    while addition_number < len(the_string): #小于字符的长度
        while i <= 2:   #每次读取两个字符　　　　
            if addition_number > len(the_string) - 1: # 当读取的字符数大于总长度 - 1
                break
            else:
                str1 = str1 + l[addition_number]  #将读取的字符拼接
                addition_number += 1
            i += 1
        list1.append(str1)
        str1 = ""
        i = 1
    return list1


if __name__ == '__main__':
    number = input("请输入(字符串或数字）: ")
    # 判断输入字符串字符个数的奇偶，奇数在最末尾补*号，并返回列表
    if len(str(number)) % 2 == 0:
        pass  # Even
    else:
        number = str(number) + "*"  # Odd

    print(string_pairs(number))
