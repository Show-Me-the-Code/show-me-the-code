#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''任一个英文的纯文本文件，统计其中的单词出现的个数'''

import re

def word_counter(filename):
    with open(filename) as f:
        text=f.read()
    #匹配文本中的单词
    words=re.findall(r'[a-zA-Z]+',text)
    #存放单词及其出现次数的字典
    result={}
    #遍历每个单词并计数
    for word in words:
        result.setdefault(word,0)
        result[word]+=1
    print result

if __name__=='__main__':
    word_counter('input_text.txt')
