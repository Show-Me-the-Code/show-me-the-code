#!/bin/env python
# -*- coding: utf-8 -*- 

'''你有一个目录，放了你一个月的日记，都是 txt，
   假设内容都是英文，请统计出你认为每篇日记最重要的词'''

import re,glob

#得到当前目录里所有日记的列表
def get_bloglist():
    return glob.glob('*.txt')

#单词计数函数
def word_counter(blog):
    #用来存放单词及其出现次数的字典
    counter={}
    with open(blog,'r') as f:
        article=f.read()
    #得到日记中所以的单词，以列表形式返回
    words=re.findall(r'[\w]+',article)
    #记录每个单词并计数
    for word in words:
        counter.setdefault(word,0)
        counter[word]+=1
    #转换字典的键-值，即键为次数，值为单词
    counter={counter[key]:key for key in counter}
    #将出现次数最多的单词及其出现次数以元组形式返回
    return (counter[max(counter)],max(counter))
   
#主函数
def main():
    n=1
    for blog in get_bloglist():
        word,times=word_counter(blog)
        print '第%d篇blog中出现最多的单词为：'%n,word,str(times)+'次'
        n+=1

if __name__=='__main__':
    main()
