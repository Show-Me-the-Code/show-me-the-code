#!/usr/bin/env python
__author__ = 'Albino'

"""
将 第 0016 题中的 number.xls 文件中的内容写到 number.xml 文件中
"""

import xlrd
import xml.dom.minidom as md


def get_xls_data(filename):
     book = xlrd.open_workbook(filename)
     sheet = book.sheet_by_index(0)
     content = []
     for i in range(sheet.nrows):
         content.append(sheet.row_values(i))
     return content


def write_to_xml(xlscontent):
    xmlfile = md.Document()
    root = xmlfile.createElement('root')
    numbers = xmlfile.createElement('numbers')
    xmlfile.appendChild(root)
    root.appendChild(numbers)
    comment = xmlfile.createComment('数字信息')
    numbers.appendChild(comment)
    xmlcontent = xmlfile.createTextNode(str(xlscontent))
    numbers.appendChild(xmlcontent)
    with open('number.xml', 'wb') as f:
        f.write(xmlfile.toprettyxml(encoding='utf-8'))


if __name__ == '__main__':
    write_to_xml(get_xls_data('number.xls'))