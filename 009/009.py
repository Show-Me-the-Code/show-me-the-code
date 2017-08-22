#!/usr/bin/env python
__author__ = 'Albino'

"""
一个HTML文件，找出里面的链接。
"""

from bs4 import BeautifulSoup


def find_the_link(filepath):
    lines = []
    with open(filepath, mode='r', encoding='utf-8') as f:
        content = BeautifulSoup(f, 'lxml')
        result = content.find_all('a')
        for i in result:
            lines.append(i['href'])
    return lines

if __name__ == '__main__':
    file_text = find_the_link("index_page.html")
    with open("file_text.txt", mode="a", encoding="utf-8") as f:
        for link in file_text:
            f.write(link + "\n")

