# -*- coding: utf-8 -*-
'''
    在你的头像上加上数字，像微信的消息提示一样。
'''
from PIL import Image,ImageFont,ImageDraw
import random

def add_num(image_path):
    img=Image.open(image_path)
    x,y=img.size                                        #得到头像的宽和高
    draw=ImageDraw.Draw(img)
    text=str(random.randint(1,99))                      #产生随机数字并字符化
    myfont=ImageFont.truetype('Futura.ttf',100)         #初始text的字体类型和尺寸
    draw.text((x*3/4,0),text,font=myfont,fill='red')    #修改图像
    
    img.save('result.jpg','jpeg')                       #保存
    
if '__name__'=='__main__':
    add_num('pic.jpg')
    
