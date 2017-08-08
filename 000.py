#!/usr/bin/env python
__author__ = 'Albino'

"""
将你的图片右上角加上数字
"""

import random
from PIL import Image, ImageFont, ImageDraw

img_num = str(random.randint(1, 99))
img = Image.open('a_sheep.png')
w, h = img.size
x = w * 0.5
y = 0
font = ImageFont.truetype("impact.ttf", 30)
text = ImageDraw.Draw(img).text((x, y), img_num, (255, 0, 0), font)
img.save('a_sheep_num.png')
