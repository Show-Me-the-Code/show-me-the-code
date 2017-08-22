#!/usr/bin/env python
__author__ = 'Albino'

'''
通常，登陆某个网站或者
APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用Python对密码加密。
'''

import os

from hashlib import sha256
from hmac import HMAC


def encrypt_password(password, salt=None):
    if not salt:
        salt = os.urandom(8)
    if isinstance(password, str):
        password = password.encode("utf-8")
    #digest()返回二进制数据字符串
    encrypt = HMAC(password, salt, sha256).digest()
    return salt + encrypt


def validate_password(hashed, password):
    # print(hashed[:8])
    return hashed == encrypt_password(password, hashed[:8])


if __name__ == "__main__":
    password_new = input("Set your password > ")
    password_saved = encrypt_password(password_new)
    password_again = input("Now,type in your password > ")
    print("Yes,you got it." if validate_password(password_saved, password_again) else "No,it's wrong.")