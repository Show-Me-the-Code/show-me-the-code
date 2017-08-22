#!/usr/bin/env python
__author__ = 'Albino'

"""
纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示
请将上述内容写到 city.xls 文件中
"""

import os
import json
import xlwt


def read_txt(path):
    with open(path, mode='r', encoding="utf-8") as f:
        text = f.read()
        text_json = json.loads(text)
    print(text_json)
    return text_json


def save_into_excel(content_dict, excel_name):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("city", cell_overwrite_ok=True)
    row = 0
    col = 0
    for v, k in sorted(content_dict.items(), key=lambda x: x[0]):
        ws.write(row, col, v)
        col = 1
        ws.write(row, col, k)
        row += 1
        col = 0
    wb.save(excel_name)


if __name__ == "__main__":
    read_content = read_txt(os.path.join(os.getcwd(), 'city.txt'))
    save_into_excel(read_content, 'city.xls')
