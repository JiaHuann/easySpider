from bs4 import BeautifulSoup
import requests
import re
import sys
import urllib.request,urllib.error
for i in range(2,29):
    a="https://writeup.ctfhub.com/archives/page/"+str(i)+"/"
    print(a)
    html = requests.get(a)
    print(html)
    html.encoding = "utf-8"
    myhtml = html.text
    #print(myhtml)
    f = open("test.html",'w')
    f.write(myhtml)

    file = open("test.html","r") #打开-html文档   rb以二进制格式读取
    html = file.read() #对file文件进行读取,读到内存里
    bs = BeautifulSoup(html,"html.parser")#用html.parser解析器对这个进行一个解析,形成了一个文件树
    t_list=bs.find_all("a", class_="post-title-link")
    for tag in t_list:
        link = 'https://writeup.ctfhub.com'+tag.get('href')+' '+tag.span.string
        f = open("spider.txt",'a')
        f.write(link)
        f.write('\r')
        print(link)
