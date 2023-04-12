# 开发时间：2023-03-21 22:09
# 开发人员：林坚洪
# encodeing "UTF-8"

import requests
from lxml import etree
import csv
import time
from selenium import webdriver

brower = webdriver.Chrome()

# print(brower.page_source)
# brower.close()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cookie': 'cookies',
    'referer': ''
}

f = open('bilibili_pc.csv', 'a', encoding='utf-8')

f.write('视频标题，up主，播放次数，弹幕数量，描述\n')
date1 = '2019-03-29 18:00:00'
timeArray = time.strptime(date1, "%Y-%m-%d %H:%M:%S")
timestamp = time.mktime(timeArray)
num1 = ((time.time() - timestamp) / 60 / 60 / 24 / 7)
num2 = int(num1 + 1)

for i in range(0, 4):
    url = 'https://www.bilibili.com/v/popular/weekly?'
    str1 = 'num=' + str(num2 - i) + ''
    url = url + str1
    brower.get(url)
    print('正在抓取页面', url)
    htm = requests.get(url, headers=headers1)
    # print(htm.text)
    htm.encoding = 'gbk'
    selector = etree.HTML(brower.page_source)
    '/html/body/div[3]/div/div[2]/div[2]/div/div/'
    shipinlist = selector.xpath('/html/body/div[3]/div/div[2]/div[2]/div/div')
    for shipin in shipinlist:
        try:
            ms = shipin.xpath('div[2]/div/span[2]/span/text()')[0]  # 描述
            upz = shipin.xpath('div[2]/div/span[1]/span/text()')[0]  # up主
            bfcs = shipin.xpath('div[2]/div/p/span[1]/text()')[0]  # 播放次数
            dmsl = shipin.xpath('div[2]/div/p/span[2]/text()')[0]  # 弹幕数量
            spbt = shipin.xpath('div[2]/p/text()')[0]  # 视频标题
            tpdz = shipin.xpath('div[1]/a/img/@data-src')[0]  #
            '/html/body/div[3]/div/div[2]/div[2]/div/div[1]/'
            spbt = str(spbt.strip().replace('\r', '').replace('\n', '').replace(' ', ''))
            upz = str(upz.strip().replace('\r', '').replace('\n', '').replace(' ', ''))
            bfcs = str(bfcs.strip().replace('\r', '').replace('\n', '').replace(' ', ''))
            dmsl = str(dmsl.strip().replace('\r', '').replace('\n', '').replace(' ', ''))
            ms = str(ms.strip().replace('\r', '').replace('\n', '').replace(' ', ''))
            tpdz = 'https:' + str(tpdz.strip().replace('\r', '').replace('\n', '').replace(' ', ''))
        except:
            continue
        temp = {
            'shipinbiaoti': spbt,
            'upzhu': upz,
            'bofancishu': bfcs,
            'danmushuliang': dmsl,
            'miaoshu': ms
        }
        try:
            f.write('{shipinbiaoti},{upzhu},{bofancishu},{danmushuliang},{miaoshu}\n'.format(**temp))  # 写入文件
            img_content = requests.get(tpdz).content
            k = open('bilibili\\' + spbt + '.jpg', 'wb')
            k.write(img_content)
        except:
            continue
        print('正在抓取：', spbt)
