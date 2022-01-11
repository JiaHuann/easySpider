urllib学习
import urllib.request
********************************************************
#获取一个get请求方法的目录
response = urllib.request.urlopen("https://writeup.ctfhub.com/categories/Skill/Web/")
print(response.read().decode("utf-8"))
#把源码封装到了对象里面   
#如果不加.decode("utf-8")会导致里面很多东西乱码,得不到很好的解释

******************************************************
#获取一个post请求
#模拟用户真实登录(可以加上cookie)
import urllib.request
import urllib.parse #引入解析器,对键值对进行封装,然后再调用byte进行二进制处理
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding = "utf-8")
response = urllib.request.urlopen("http://httpin.org/w",data = data)#可选timeout,即多长时间内没有请求
print(response.read().decode("utf-8"))

#发出去的时候useragent会"自曝",自己是python脚本,如果网站有饭爬机制的话,就不行了 
import urllib.request
response = urllib.request.urlopen("http://www.baidu.com")#可选timeout,即多长时间内没有请求
print(response.read().decode("utf-8"))

******************************************************8
异常处理(超时)
try:
	response = urllib.request.urlopen("http://www.baidu.com",timeout = 0.01)#可选timeout,即多长时间内没有请求
	print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
	print("????????")

*********************************************************
#数据初步处理:对response对象的处理,集成了很多东西,可以自由调用比如:
print(response.getheads())
#甚至是对一个键值对的调用(去掉s)
print(response.gethead("Server"))


**********************************************************
反反爬虫    思路:模拟浏览器发送请求头,利用Request进行request对象封装
所以不能像上面一样直接用urlopen打开链接,然后用urllib.request封装成对象

url = "https://douban.com"
header = {
	#用来模拟的信息(主要是useragent)
}
data = bytes(urllib.parse.urlencode("你要发的数据"),encoding = "utf-8")
req = urllib.request.Request(url = url,data = data,headers = headers,method = "POST")
response = urllib.urlopen(req)
print(req.read().decode("utf-8"))
