#!/usr/bin/env python
__author__ = 'Albino'

"""
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""

import os
from PIL import Image

iPhone5_WIDTH = 1136
iPhone5_HEIGHT = 640


def walk(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith("jpg"):
                picture_path = os.path.join(path, file)
                new_picture_name = "iPhone5_" + file
                new_picture(picture_path, new_picture_name)


def new_picture(path, name, width=iPhone5_WIDTH, height=iPhone5_HEIGHT):
    img = Image.open(path)
    w, h = img.size
    if w > width:
        h = w * h // width
    if h > height:
        w = w * h // height
    img_resize = img.resize((w, h), Image.ANTIALIAS)
    img_resize.save('./new_image/' + name)

if __name__ == '__main__':
    walk(os.path.join(os.getcwd(), 'image'))
