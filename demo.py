#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/20 09:22
# @Author  : Puxf
# @Site    : 
# @File    : demo.py
# @Software: PyCharm


from bs4 import BeautifulSoup
import requests
import sys


# if __name__ == '__main__':
#     target = 'http://book.zongheng.com/showchapter/1098128.html'
#     req = requests.get(url=target)
#     html = req.text
#     bf = BeautifulSoup(html,features='html.parser')
#     div = bf.find_all('div',class_='volume-list')
#     print(div[0])

#获取章节链接
# if __name__ == '__main__':
#     target = 'http://book.zongheng.com/showchapter/1098128.html'
#     req = requests.get(url=target)
#     html = req.text
#     ul_bf = BeautifulSoup(html,features='html.parser')
#     ul = ul_bf.find_all('ul',class_='chapter-list clearfix')
#     a_bf = BeautifulSoup(str(ul),features='html.parser')
#     a = a_bf.find_all('a')
#     for each in a[1:]:
#         print(each.string,each.get('href'))


# if __name__ == '__main__':
#     target = 'http://book.zongheng.com/showchapter/1098128.html'
#     req = requests.get(url=target)
#     html = req.text
#     li_bf = BeautifulSoup(html,features='html.parser')
#     li = li_bf.find_all('li',class_ = 'col-4')
#     a_bf = BeautifulSoup(str(li),features='html.parser')
#     a = a_bf.find_all('a')
#     for each in a:
#         print(each.string,each.get('href'))



"""整合代码"""

class downloader (object):

    def __init__(self):
        self.target = 'http://book.zongheng.com/showchapter/1098128.html'
        self.names = []
        self.urls = []
        self.nums = 0
    """获取章节下载链接"""

    def get_download_url(self):
        req = requests.get(url=self.target)
        html = req.text
        ul_bf = BeautifulSoup(html, features='html.parser')
        ul = ul_bf.find_all('ul', class_='chapter-list clearfix')
        a_bf = BeautifulSoup(str(ul), features='html.parser')
        a = a_bf.find_all('a')
        self.nums = len(a)
        for each in a:
            self.names.append(each.string)
            self.urls.append(each.get('href'))
    """获取章节内容"""
    def get_contents(self,target):
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html,features='html.parser')
        texts = bf.find_all('div',class_='content')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts
    """文章内容写入文件"""
    def writer(self,name,path,text):
        writer_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    for i in range(dl.nums):
        dl.writer(dl.names[i],'法学院的新生.txt',dl.get_contents(dl.urls[i]))
        sys.stdout.write("   已下载:%.3f%%" % float(i / dl.nums) + '\r')
        sys.stdout.flush()
    print('《法学院的新生》下载完成')










