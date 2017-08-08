#!/usr/bin/env python
__author__ = 'Albino'

"""
使用 Python 如何生成 200 个激活码
"""

import random
import string


ALL_LETTER = string.digits + string.ascii_uppercase
CODE_ROUND = 10
CODE_CONTENT = 200
CODE_LIST = []
while len(CODE_LIST) != CODE_CONTENT:
    EVERY_CODE = "".join(random.choice(ALL_LETTER) for x in range(CODE_ROUND))
    if EVERY_CODE not in CODE_LIST:
        CODE_LIST.append(EVERY_CODE)


def write_txt(file, list):
    with open(file, mode='a',encoding='utf-8') as f:
        for line in list:
            f.write(line + "\n")


write_txt("code_list.txt", CODE_LIST)
print(len(CODE_LIST))
print(CODE_LIST)
