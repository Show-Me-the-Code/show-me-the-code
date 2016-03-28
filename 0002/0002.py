#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''将随机码存入mysql'''

import mysql.connector

#读取文件
def file_read(filename):
    #从文件中读取每行的码
    codes=[]
    with open(filename,'r') as f:
        lines=f.readlines()
    for n in range(200):
        #去除每行的空白符
        codes.append(lines[n].strip())
    return codes

#存入数据库
def store():
    codes=file_read('codes.txt')
    conn=mysql.connector.connect(user='root',password='666666',database='test',use_unicode=True)
    cursor=conn.cursor()
    cursor.execute('create table codes(id int(3) primary key,code varchar(6))')
    for n in range(200):
        cursor.execute('insert into codes (id,code) values (%s,%s)',[n+1,codes[n]])
    conn.commit()
    cursor.close()
    conn.close()
    print 'finish'

if __name__ == '__main__':
    store()
