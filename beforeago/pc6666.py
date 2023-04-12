# 下面的包不一定全部都会用到
from concurrent.futures import thread
import threading
import time
import re
import os
import requests

k = "https://.html"  # 需要爬取图片的网页地址
fPage = requests.get(k)  # 得到网页源码
fPage.encoding = 'utf-8'  # 这里是为了爬标题，有些中文标题爬下了是乱码
page = fPage.text  # 获取网页内容
# print(page)
pag = page.split('<div class="content_left">')[1].split('<div class="nav-links page_imges"> </div>')[
    0]  # 这里是通过字符串分割获取图片的位置，可以自己选择
title = re.findall('<title>(.*)</title>', page)[0]  # 获取网页标题

res = re.compile(r"src='(http.+?.jpg)'")  # 运用正则表达式过滤出图片路径地址
# python的正则我不太怎么清楚，毕竟我是菜鸟
# 我的写法是这样的
# https://i0.hdslb.com/bfs/face/1.jpg
# https://i0.hdslb.com/bfs/face/2.jpg
# https://i0.hdslb.com/bfs/face/3.jpg
# 把上面123的位置缓存.+?就行了，
reg = re.findall(res, pag)  # 匹配网页进行搜索出图片地址数组
print(title)
# 下载文件
num = 1
exitFlag = 0


# 下面是print_time是根据图片地址保存文件
class myThread(threading.Thread):
    def __init__(self, threadID, nums):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.nums = nums

    def run(self):
        # print ("开始线程：" + self.name)
        print_time(self.threadID, self.nums)
        # print ("退出线程：" + self.name)


def print_time(threadID, nums):
    # threadID其实就是地址链接
    response = requests.get(threadID)
    # 此处相当于文件路径/数字.jpg
    filename = dirname + '/' + str(nums) + ".jpg"
    with open(filename, 'wb') as f:
        f.write(response.content)
        f.close()
    print("第%s张照片下载成功" % nums)


# 创建名为网页标题的文件夹
dirname = title
if not os.path.exists(dirname):  # 文件夹不存在的时候在创建
    os.makedirs(dirname)
threads = []  # 用于退出线程
for item in reg:  # reg是包含多个图片链接的数组
    # 通过循环创建多个线程去爬图
    thread1 = myThread(item, num)
    thread1.start()  # 开启线程
    threads.append(thread1)
    num = num + 1
for i in threads:
    i.join()  # 退出线程
print("退出主线程")