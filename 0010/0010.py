#!/usr/bin/env python
#-*- coding: utf-8 -*-
import Image, ImageDraw, ImageFont, ImageFilter
import random
import string

# 随机字母:
def rnd_letter():
    return random.choice(string.letters)

# 随机背景颜色:
def bg_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机字体颜色:
def letter_color():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 图片尺寸240 x 60:
width = 60 * 4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 40)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=bg_color())
# 输出文字:
for t in range(4):
    draw.text((60*t+15, 15), rnd_letter(), font=font, fill=letter_color())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('result.jpg', 'jpeg')
