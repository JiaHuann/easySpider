BeautifulSoup

将复杂的html转化成一个复杂的树形结构,每个节点都是一个python对象,所有对象可以归纳为4种
1  TAG   2 NavigableString   3 BeautifulSoup  4 Comment 



*********************1111111111111111111111****************************************
from bs4 import BeautifulSoup
file = open ("./baidu.html","rb") #打开-html文档   rb以二进制格式读取
html = file.read() #对file文件进行读取,读到内存里
bs = BeautifulSoup(html,"html.parser")#用html.parser解析器对这个进行一个解析,形成了一个文件树
print(bs.title)#bs.a  bs.head       bs.标签名(第一次出现)


对于bs.head进行一个type的查询问,可知是bs4.element.Tag类型的对象
BUT 只能拿到第一个结果

**************************22222222222222222222**************************************
print(bs.title.string)#类型是NavigableString  标签里的内容 也就是字符串

****************************************************************
print(bs.title.attrs)#拿到一个标签里所有的KV串,也就是各种属性和值
如{'class':['mnav'],'herf':'http://news.baidu.com','name':'xxxxxx'}
***********************3333333333333333333333******************************************
print(bs)
对bs本身进行一个type查询,发现他自身就是beautifulsoup类型的对象
表示整个文档
*********************444444444444444444********************************************
print(bs.a.string)    #对注释进行一个替换



########################################################################
应用
print(bs.head.contents)#拿到head标签下,所有meta content并放在contents数组里面
对不同的meta content标签的调用可以使用 bs.head.contents[i]调用

更多的内置调用,可以查看beautifulsoup文档进行查看


######################################################################
文档的搜索

1.find_all
**********************字符串过滤
t_list = bs.find_all("a")
print(t_list)#生成一个以,链接的所有a标签


*********************正则表达式搜索		使用search()
import re
t_list = bs.find_all(re.compile("a"))

*********************方法搜索(传入函数)
def name_is_exist(tag):#只要标签里面有name都可以被匹配
	return tag.has_attr("name")
t_list = bs.find_all(name_is_exist)

按照列表打印
for item in t_list:
	print(item)

***********************************************
2.kwawrgs特定参数查找
t_list = bs.find_all(id="head")
返回这个id下的所有标签1

t_list = bs.find_all(class_=True)#意思是只要有class这个参数就行
***************************************************
3.text参数
t_list = bs.find_all(text = "hao123")#找特定文本的一个内容

多个text查找
t_list = bs.find_all(text =["hao123","baidu"])
for item in t_list:
	print(item)



应用正则表达式来找特定文本的内容
t_list = bs.find_all(text =re.compile("xxxx"))
*****************************************************
4.limit 参数    限制获取多少个
*****************************************************
.select方法


小知识:选择器
利用css选择器
通过id,class定位一堆东西
t_list = bs.select(".类名")
t_list =bs.select("#u1")

通过标签
t_list = bs.select("标签名字")

双重精确 具体到某个标签的某个属性
t_list = bs.select("a[class='bri']")  

父子查找
t_list=bs.select("head > title")

同级兄弟节点的查找
t_listbs.select(".mnav ~ .bri")#是.mnav选择器的是bri选择器的兄弟标签
