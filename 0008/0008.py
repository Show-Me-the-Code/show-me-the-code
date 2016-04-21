#!/usr/bin/python
#-*- coding=utf-8 -*-

"""
    一个HTML文件，找出里面的正文
"""

from bs4 import BeautifulSoup
import urllib2

def get_content(url):
    html=urllib2.urlopen(url)
    soup=BeautifulSoup(html)
    content=soup.get_text().split('\n')
    #遍历每一行，打印出有内容的行
    for line in content:
        if not line:
            continue
        print line

if __name__=='__main__':
    print get_content('http://nba.hupu.com/')
