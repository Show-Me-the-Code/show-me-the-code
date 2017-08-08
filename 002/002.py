#!/usr/bin/env python
__author__ = 'Albino'

"""
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
"""

import MySQLdb


def store_mysql(filepath):
    db = MySQLdb.connect(user='root', password='', host='localhost', db='showmethecode')
    cursor = db.cursor()
    cursor.execute("show tables in showmethecode")
    tables = cursor.fetchall()
    flag = False
    for table in tables:
        if "code" in table:
            flag = True
            print("this table is readly existed")
    if not flag:
        cursor.execute("""
                            CREATE TABLE code(
                                id INT NOT NULL AUTO_INCREMENT,
                                code VARCHAR (10),
                                PRIMARY KEY (id)
                            )""")
    with open(filepath, mode='r', encoding='utf-8')as f:
        lines = f.readlines()
        for line in lines:
            coupon = line.strip()
            cursor.execute("INSERT INTO code(code) VALUE (%s)", [coupon])
    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    store_mysql('code_list.txt')
