# 开发时间： 2023/01/17
# 开发人员：林坚洪
import requests
#搜狗图片 下载一张
import requests
from bs4 import BeautifulSoup
import time

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
}

def down1():
    for i in range(1, 3):
        url = "https://wallhaven.cc/search?categories=111&purity=010&topRange=1M&sorting=toplist&order=desc&page=" + str(i) + ".html"
        # url = "https://699pic.com/originality-0-176-" + str(i) + ".html"
        down2(url)

def down2(neirong):
    r = requests.get(neirong, headers=header)
    r.encoding = "utf-8"  #r.apparent_encoding
    print(r.status_code)
    demo = r.text
    # print(demo) #查看网页的内容
    down3(demo)

def down3(biaoqian):
    soup = BeautifulSoup(biaoqian, "html.parser")
    tags = soup.find_all("img", class_="preview")
    print(len(tags)) #查看找到的标签数量
    # print(tags) #查看标签内容
    for tag in tags:
        image = "https:" + tag["data-original"]
        print(image)
        down4(image)

def down4(shuchu):
    print(time.time())
    fileName = "image/" + str(int(time.time() * 1000)) + ".jpg"
    r = requests.get(shuchu, headers=header)
    f = open(fileName, "wb")
    f.write(r.content)
    f.close()

if __name__ == "__main__":
    down1()
