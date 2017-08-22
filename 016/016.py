#!/usr/bin/env python
__author__ = 'Albino'

"""
纯文本文件 numbers.txt, 里面的内容写到 numbers.xls 文件中
"""

import os
import json
import xlwt


def read_txt(path):
    with open(path, mode='r', encoding="utf-8") as f:
        text = f.read()
        text_json = json.loads(text)
    return text_json


def save_into_excel(content_list, excel_name):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("numbers", cell_overwrite_ok=True)
    row = 0
    col = 0
    for i in content_list:
        for j in i:
            ws.write(row, col, j)
            col += 1
        col = 0
        row += 1
    wb.save(excel_name)


if __name__ == "__main__":
    read_content = read_txt(os.path.join(os.getcwd(), 'numbers.txt'))
    save_into_excel(read_content, 'number.xls')