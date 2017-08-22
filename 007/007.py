#!/usr/bin/env python
__author__ = 'Albino'

"""
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""

import os


def walk_dir(path):
    file_path = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith("py"):
                file_path.append(os.path.join(path, file))
    return file_path


def count_the_code(path):
    file_name = os.path.basename(path)
    code_num = 0
    blank_num = 0
    note_num = 0
    flag = False
    with open(path, mode='r', encoding='utf-8') as f:
        lines = f.read().split('\n')
        for line in lines:
            code_num += 1
            if line.strip().startswith('"""') and not flag:
                note_num += 1
                flag = True
                continue
            if line.strip().startswith('"""'):
                note_num += 1
                flag = False
            if line.strip().startswith('#') or flag:
                note_num += 1
            if len(line) == 0:
                blank_num += 1
    print("在%s中，共有%s行代码，其中有%s空行，有%s注释" % (file_name, code_num, blank_num, note_num))


if __name__ == '__main__':
    for code_path in walk_dir("."):
        count_the_code(code_path)
