#!/usr/bin/env python
__author__ = 'Albino'

"""
纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
请将上述内容写到 student.xls 文件中
# cell_overwrite_ok 可以让用户可以重复写内容
"""

import os
import json
import xlwt


def read_txt(path):
    with open(path, mode='r', encoding='utf-8') as f:
        text = f.read()
        text_json = json.loads(text)
    return text_json


def save_into_excel(content_dict):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('student',cell_overwrite_ok=True)
    row = 0
    col = 0
    for k, v in sorted(content_dict.items(), key=lambda x:x[0]):
        ws.write(row, col, k)
        for i in v:
            col += 1
            ws.write(row, col, i)
        row += 1
        col = 0
    wb.save('students.xls')


if __name__ == "__main__":
    read_content = read_txt(os.path.join(os.getcwd(), "student.txt"))
    save_into_excel(read_content)
