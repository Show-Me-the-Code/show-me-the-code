#!/usr/bin/env python
__author__ = 'Albino'

"""
一个HTML文件，找出里面的正文。
"""

from bs4 import BeautifulSoup


def find_the_content(path):
    with open(path, mode='r', encoding='utf-8') as f:
        content = BeautifulSoup(f, 'lxml')
        text = content.get_text().strip()
        return text


if __name__ == '__main__':
    file_text = find_the_content("index_page.html")
    with open('file_text.txt', mode='a', encoding='utf-8') as f:
        f.write(file_text)
