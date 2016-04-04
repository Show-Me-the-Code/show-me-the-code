#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。空行和注释要分别列出来。
"""
import glob
import os

def get_file_pathes():
    return glob.glob('*.py')

def codes_count(path):
    code_line=comment_line=blank_line=0
    with open(path,'r') as f:
        lines=f.readlines()
    flag=False
    for line in lines:
        #如果该行为空行
        if not line.strip():
            blank_line+=1
        
        #如果为多行注释，则将flag置”1“
        elif line.strip().startswith(('\"\"\"',"\'\'\'")) and not flag:
            comment_line+=1
            flag=True
            continue
        #如果为多行注释的末行，则把flag置”0“
        elif line.strip().endswith(('\"\"\"',"\'\'\'")) and flag:
            comment_line+=1
            flag=False

        #如果该行为单行注释，或者多行注释里的内容
        elif line.strip().startswith('#') or flag :
            comment_line+=1 
        #否则为代码行
        else:
            code_line+=1
    return code_line,comment_line,blank_line

def main():
    for path in get_file_pathes():
        #得到文件的名字
        file_name=os.path.basename(path)
        results=codes_count(path)
        print '在%s文件中，代码行数为:%d 注释行数为:%d 空行数为:%d'%(file_name,results[0],results[1],results[2])

if __name__=='__main__':
    main()
