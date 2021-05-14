#!/usr/bin/env python
# -*- coding: UTF-8 -*-


alphabet_src = 'abcdefghijklmnopqrstuvwxyz'
alphabet_tar = alphabet_src[::-1]


src_str = input("请输入需要加密的字符串：")

encrypted_str= ''
for single_char in src_str:
    if single_char in alphabet_src:
        index = alphabet_src.index(single_char)
        encrypted_str = encrypted_str + alphabet_tar[index]
    else:
        encrypted_str = encrypted_str + single_char
print(encrypted_str)


if __name__ == '__main__':
    pass
