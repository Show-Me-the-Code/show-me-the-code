#!/usr/bin/env python
__author__ = 'Albino'

"""
你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，
假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""

import os
import re

from collections import Counter


def walk_dir(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith("txt"):
                file_list.append(os.path.join(path, file))
    return file_list


def find_key_word(filepath):
    file_name = os.path.basename(filepath)
    with open(filepath, mode='r', encoding='utf-8') as f:
        text = f.read().lower().strip()
        pattern = '[a-zA-Z]+'
        word = re.findall(pattern, text)
        result = sorted(Counter(word).items(), key=lambda x : x[1])
        print("在%s文件中，%s为关键字，共出现%s次" % (file_name, result[-1][0], result[-1][1]))


if __name__ == "__main__":
    for file_path in walk_dir(os.path.join(os.getcwd(), 'diary')):
        find_key_word(file_path)
