#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/18 16:50
# @Author  : Puxf
# @Site    : 
# @File    : Batch modify file suffix.py
# @Software: PyCharm


import os.path
#获取需修改的文件路径
path = r'D:\Python_test_dir'
file_name = os.listdir(path)
count = 0
for name in file_name:
    port = os.path.splitext(name)
    newname = port[0]+ '.bmp'
    os.rename(os.path.join(path,name),os.path.join(path,newname))
    count += 1
    print(name)
print('一共修改了'+str(count)+'个文件')







