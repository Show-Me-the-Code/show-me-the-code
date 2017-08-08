#!/usr/bin/env python
__author__ = 'Albino'

"""
敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」
"""


def trans_to_words():
    type_in = str(input(">")).lower()
    with open("filtered_words.txt", mode="r", encoding="utf-8") as f:
        text = f.read().split("\n")
        for i in text:
            if i in type_in:
                type_in = type_in.replace(i, '**')
    print(type_in)


if __name__ == "__main__":
    trans_to_words()