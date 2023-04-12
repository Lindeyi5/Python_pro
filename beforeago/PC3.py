# 开发时间：2023-01-18 17:44
# 开发人员：林坚洪
#导入两个开发库
import urllib.request
from bs4 import BeautifulSoup
#定义图像的url地址（就是你想要爬取的网址）
domain = 'https://wallhaven.cc/search?categories=111&purity=010&topRange=1M&sorting=toplist&order=desc/'
#在大多数网站都会有反爬取机制，所以我们这里以修改UserAgent的方式来模拟浏览器的形式来骗过该机制
req = urllib.request.Request(domain)
req.add_header('Host','wallhaven.cc/search?categories=111&purity=010&topRange=1M&sorting=toplist&order=desc')
req.add_header('Referer','https://wallhaven.cc/search?categories=111&purity=010&topRange=1M&sorting=toplist&order=desc/')
req.add_header('User-Agent','fake-client')
#接下来通过urllib.request的urlopen()函数来打开网页并发出请求，获得数据，再通过read()函数读取获得的数据，代码如下：
html = urllib.request.urlopen(req)
info = html.read()
print('打印info','\n',info)#将结果打印出来，验证是否成功
soup = BeautifulSoup(info,'html.parser')
#这里使用开发库BeautifulSoup4的一个类BeautifulSoup，来实例化我们的对象info，
#让其相当于一个页面，使其HTML页面结构成为BeautifulSoup的属性，
#函数的第二个参数是指定使用HTML解释器
all_img = soup.find_all('img',class_ = 'preview')#通过find_all()函数进行筛选，筛选条件是img标签并且表示属性class为i71-img
print("打印all_img",all_img)#打印输出筛选出的图片信息
#使用for循环遍历all_img来定义下载后图片的名称，再使用urllib.request.urlretrieve()函数来下载图片
i=0
for img in all_img:
    i=i+1
    image_name = '%s.jpg' % i
    #设置图片的保存位置，记得提前创建好文件夹，有能力的可以通过python来自动创建
    urllib.request.urlretrieve('https:'+img['src'],'C:\\D\\12345\\'+image_name)
    print('第%s张下载完成' %i,image_name)
print('下载完成')


