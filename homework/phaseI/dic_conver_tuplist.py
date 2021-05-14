#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def dic_tuplist(Adict):
    """
    Given dictionary
    """
    # Using in
    Alist=[(key,val) for key, val in Adict.items()]
    return Alist

def dic_tuplist_zip(Alist):
    """
    zip函数将传递给它的项目组合为参数。将字典的键和值作为zip函数的参数，
    并将结果放在list函数下。键值对成为列表的元组。
    """
    Alist = list(zip(Adict.keys(), Adict.values()))
    return Alist

def dict_tuplist_append(Adict):
    """
    带append
    采用一个空列表并将每个键值对附加为元组。for循环用于将键值对转换为元组。
    """
    Alist= []
    # Uisng append
    for x in Adict:
        k = (x, Adict[x])
        Alist.append(k)
    return Alist


if __name__ == '__main__':
    Adict = {"foo": "bar", "key": "value"}
    print(f"The give Dict： {Adict}")
    #in
    print(f"The list of tuples: {dic_tuplist(Adict)}")
    # zip
    print(f"The list of tuples: {dic_tuplist_zip(Adict)}")
    # append
    print(f"The list of tuples: {dict_tuplist_append(Adict)}")

