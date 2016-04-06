#!/bin/env python
#-*- coding: utf-8 -*-

"""
敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
当用户输入敏感词语，则用星号*替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」
"""

#读取文件，将敏感词语以列表形式返回
def file_read(filename):
    words=[]
    with open(filename,'r') as f:
        for word in f.read().split('\n'):
            words.append(word)
    return words

#检查用户输入中是否有敏感词，如果有则将输入做处理后返回
def Check(words,string):
    for word in words:
        if word in string:
            string=string.replace(word,'**')
    return string

#主函数
def main():
    while True:
        string=raw_input('please enter u sentance: ')
        if string=='exit':
            break
        words=file_read('filtered_words.txt')
        print Check(words,string)

if __name__ == '__main__':
    main()
