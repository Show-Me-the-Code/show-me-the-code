#!/usr/bin/env python
__author__ = 'Albino'

"""
将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中
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
    students = xmlfile.createElement('students')
    xmlfile.appendChild(root)
    root.appendChild(students)
    comment = xmlfile.createComment('学生信息表 "id" : [名字, 数学, 语文, 英文]')
    students.appendChild(comment)
    xmlcontent = xmlfile.createTextNode(str(xlscontent))
    students.appendChild(xmlcontent)
    with open('student.xml', 'wb') as f:
        f.write(xmlfile.toprettyxml(encoding='utf-8'))


if __name__ == '__main__':
    write_to_xml(get_xls_data('student.xls'))