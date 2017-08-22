#!/usr/bin/env python
__author__ = 'Albino'

"""
iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用。
"""

import os
from PIL import Image

PHONE = {'iPhone5':(1136,640), 'iPhone6':(1134,750), 'iPhone6P':(2208,1242)}


def walk(path, phone_type='iPhone6'):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith("jpg"):
                picture_path = os.path.join(path, file)
                new_picture_name = "iPhone5_" + file
                new_picture(picture_path, new_picture_name, phone_type)


def new_picture(path, name, phone_type):
    img = Image.open(path)
    w, h = img.size
    width, height = PHONE[phone_type]

    if w > width:
        h = w * h // width
    if h > height:
        w = w * h // height
    img_resize = img.resize((w, h), Image.ANTIALIAS)
    img_resize.save('./new_image/' + name)

if __name__ == '__main__':
    walk(os.path.join(os.getcwd(), 'image'))
