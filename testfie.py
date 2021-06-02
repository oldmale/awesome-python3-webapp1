#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/18 13:27
# @Author  : Puxf
# @Site    : 
# @File    : testfie.py
# @Software: PyCharm



import os
import os.path

#需要操作的文件夹路径并获取文件名

path = r'D:\Python_test_dir'
file_names = os.listdir(path)
#初始化count,count1
count = 0
count1 = 0

#遍历路径下的文件名
for name in file_names:
    list_str = list(name)#把遍历得到的文件名转为列表形式
    if list_str[39] == '.':#判断列表索引39等于'.'才继续
     del list_str[list_str.index('.')]#删除列表索引为39的元素
     str1 = ''.join(list_str)#将删除后得到的列表转为字符串形式
     oldname = os.path.join(path,name)#原文件名
     newname = os.path.join(path,str1)#新文件名
     os.rename(oldname,newname)#原文件名重命名为新文件名
     count+=1
    else:
        count1+=1
        print("不相同的有"+str(count1)+"个文件")
print("一共重命名"+str(count)+"个文件")