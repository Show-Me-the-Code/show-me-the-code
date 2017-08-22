#!/usr/bin/env python
__author__ = 'Albino'

"""
将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中
"""

import xlrd
import xml.dom.minidom as md


def get_xls_data(filename):
     book = xlrd.open_workbook(filename)
     sheet = book.sheet_by_index(0)
     content = {}
     for i in range(sheet.nrows):
         content[i+1] = sheet.row_values(i)[1:]
     return content


def write_to_xml(xlscontent):
    xmlfile = md.Document()
    root = xmlfile.createElement('root')
    citys = xmlfile.createElement('citys')
    xmlfile.appendChild(root)
    root.appendChild(citys)
    comment = xmlfile.createComment('城市信息')
    citys.appendChild(comment)
    xmlcontent = xmlfile.createTextNode(str(xlscontent))
    citys.appendChild(xmlcontent)
    with open('citys.xml', 'wb') as f:
        f.write(xmlfile.toprettyxml(encoding='utf-8'))


if __name__ == '__main__':
    write_to_xml(get_xls_data('city.xls'))