#!/usr/bin/env python
__author__ = 'Albino'

"""
使用 Python 生成类字母验证码图片
'arial.ttf'
"""

import string
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


IMAGE_MODE = 'RGB'
IMAGE_BG_COLOR = (255, 255, 255)
text = "".join(random.sample(string.ascii_letters, 4))


def color_random():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def create_identifying_code(text, width=400, height=200, chance=2):
    img = Image.new(IMAGE_MODE, (width, height), IMAGE_BG_COLOR)
    draw = ImageDraw.Draw(img)
    for w in range(width):
        for h in range(height):
            if chance < random.randint(1,100):
                draw.point((w, h), fill=color_random())
    font = ImageFont.truetype('arial.ttf', 80)
    str_w, str_h = font.getsize(text)
    x = (width - str_w) / 2
    y = (height - str_h) / 2
    for i in text:
        draw.text((x, y), i, font=font, fill=color_random())
        x += str_w / len(text)
    img.filter(ImageFilter.BLUR)
    img.save('code_pic.jpg')


if __name__ == '__main__':
    create_identifying_code(text)
