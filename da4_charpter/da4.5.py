# 开发时间：2023-03-16 16:30
# 开发人员：林坚洪
# encodeing "UTF-8"
import requests
from lxml import etree
import csv
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

f = open('qfang.csv', 'a', encoding='utf-8')
f.write('名称，板块，均价\n')

for i in range(1, 5):
    url = 'https://nanjing.qfang.com/rent'
    url = url + '/f' + str(i);
    htm = requests.get(url, headers=headers)
    htm.encoding = 'utf-8'
    selector = etree.HTML(htm.text)
    xiaoqulist = selector.xpath('//*[@id="cycleListings"]/ul/li')
    for xiaoqu in xiaoqulist:
        try:
            mc = xiaoqu.xpath('div[2]/div[1]/a/text()')[0]  # 小区名称
            selector2 = etree.HTML(htm.content)
            '//*[@id="cycleListings"]/ul/li[2]/div[2]/div[3]/div/text()'
            '/html/body/div[4]/div/div[1]/div[4]/ul/li[16]/div[2]/div[3]/div/text()'
            # for d in range(1, 30):
            bk2 = xiaoqu.xpath('div[2]/div[3]/div/text()')[0]
            bk = selector2.xpath('string(/html/body/div[4]/div/div[1]/div[4]/ul/li/div[2]/div[3]/div)')  # 小区板块
            bk2=str(bk2)
            bk = bk.strip().replace('\r', '').replace('\n', '').replace(' ', '')
            print(bk)
            jj = xiaoqu.xpath('div[3]/p/span[1]/text()')[0]
            jj1 = xiaoqu.xpath('div[3]/p/span[2]/text()')[0]  # 小区均价
            jj = jj + jj1
        except:
            continue
        temp = {
            'mingchen': mc,
            'bankuai': bk,
            'junjia': jj
        }
        try:
            f.write('{mingchen},{bankuai},{junjia}\n'.format(**temp))  # 写入文件
        except:
            print('写入错误！')
        print('正在抓取：', mc)
# mc=selector.xpath('//*[@class="house-title fl"]/text()')
# bk=selector.xpath('//*[@class="text fl clearfix"]/a/text()')
# bk2 = selector.xpath('//*[@class="text fl clearfix"]/text()')
# print(bk)
