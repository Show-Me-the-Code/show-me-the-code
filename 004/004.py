#!/usr/bin/env python
__author__ = 'Albino'

"""
任一个英文的纯文本文件，统计其中的单词出现的个数。
"""

import os
import re

from collections import Counter


def word_count(filename):
    with open(filename) as f:
        text = f.read().lower()
        pattern = "[a-zA-Z]+’[a-zA-Z]|[a-zA-Z]+"
        word = re.findall(pattern, text)
        result = sorted(Counter(word).items(), key=lambda x:x[1], reverse=True)
        for i in result:
            print("%s出现了%s次" % (i[0], i[1]))


if __name__ == '__main__':
    word_count("004.txt")
