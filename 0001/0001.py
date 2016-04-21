#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''生成200个长度为6的随机码'''

import random,string

#生成随机码
def generateCodes(code_amount,code_len):
    Strs=string.digits+string.letters
    codes=[]
    while(code_amount>0):
        code=''.join([random.choice(Strs) for i in range(code_len)])
        if code not in codes:
            code+='\n'
            codes.append(code)
            code_amount-=1
    return codes

#将随机码写入codes.txt    
def file_write(code_amount,code_len):
    f=open('codes.txt','w')
    for code in generateCodes(code_amount,code_len):
        f.write(code)
    f.close()

if __name__=='__main__':
    file_write(200,6)
