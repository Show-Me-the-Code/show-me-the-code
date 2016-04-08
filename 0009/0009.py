#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
    一个HTML文件，找出里面的链接
"""

import urllib2
from bs4 import BeautifulSoup

def get_link(url):
    html=urllib2.urlopen(url)
    soup=BeautifulSoup(html)
    for i in soup.find_all('a'):
        print i['href']
   
if __name__ == '__main__':
    get_link('http://nba.hupu.com/')
