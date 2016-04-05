#!/bin/env python
# -*- coding: utf-8 -*-

"""
文本文件 filtered_words.txt 里面的内容为敏感词，当用户输入敏感词语时，则打印出 Freedom，
否则打印出 Human Rights
"""

def file_read(filename):
    words=[]
    with open(filename,'r') as f:
        for line in f.readlines():
            words.append(line.strip())
    return words

def check(words):
    word=raw_input('Please enter word: ')
    if word in words:
        print 'Freedom'
    else:
        print 'Human Rights'

def main():
    check(file_read('filtered_words.txt'))

if __name__ == '__main__':
    main()
