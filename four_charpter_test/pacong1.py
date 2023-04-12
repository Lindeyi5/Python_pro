# 开发时间：2023-03-21 19:24
# 开发人员：林坚洪
# encodeing "UTF-8"


import requests
from lxml import etree
import csv
import time

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

f = open('cinema.csv', 'a', encoding='utf-8')
# f.write('电影名，主演，上映时间，评分\n')

for i in range(1, 5):
    url = 'https://www.maoyan.com/board/4?timeStamp=1679398112095&channelId=40011&index=4&signKey=071a7c48283ce73ac9fe693a39e459d3&sVersion=1&webdriver=false'
    str1 = '&offset=' + str((i - 1) * 10) + ''
    url = url + str1
    print(url)
    htm = requests.get(url, headers=headers)
    print(htm.text)
    htm.encoding = 'utf-8'
    selector = etree.HTML(htm.text)
    dianyinlist = selector.xpath('/html/body/div[4]/div/div/div[1]/dl/dd')
    for dianyin in dianyinlist:
        try:
            mz = dianyin.xpath('div/div/div[1]/p[1]/a/text()')[0]  # 电影名字
            zy = dianyin.xpath('div/div/div[1]/p[2]/text()')[0]
            sysj = dianyin.xpath('div/div/div[1]/p[3]/text()')[0]
            pf1 = dianyin.xpath('div/div/div[2]/p/i[1]/text()')[0]
            pf2 = dianyin.xpath('div/div/div[2]/p/i[2]/text()')[0]
            pf = str(pf1) + str(pf2)
            mz=str(mz.strip().replace('\r', '').replace('\n', '').replace(' ', ''))
            zy=str(zy.strip().replace('\r', '').replace('\n', '').replace(' ', ''))
            sysj=str(sysj.strip().replace('\r', '').replace('\n', '').replace(' ', ''))
            pf=str(pf.strip().replace('\r', '').replace('\n', '').replace(' ', ''))
        except:
            continue
        temp = {
            'mingchen': mz,
            'zhuyan': zy,
            'shangyinshijian': sysj,
            'pinfen': pf
        }
        try:
            f.write('{mingchen},{zhuyan},{shangyinshijian},{pinfen}\n'.format(**temp))  # 写入文件
        except:
            print('写入错误！')
        print('正在抓取：', mz)
