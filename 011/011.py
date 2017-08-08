#!/usr/bin/env python
__author__ = 'Albino'

"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，
否则打印出 Human Rights。
"""


def trans_to_words():
    type_in = str(input('>')).lower()
    with open("filtered_words.txt", mode='r', encoding='utf-8') as f:
        text = f.read().split("\n")
        flag = False
        for line in text:
            if line in type_in:
                flag = True
        if flag:
            print("Freedom")
        else:
            print("Human Right")


if __name__ == "__main__":
        trans_to_words()
