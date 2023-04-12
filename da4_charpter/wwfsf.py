# 开发时间：2023-03-17 10:43
# 开发人员：林坚洪
# encodeing "UTF-8"
import requests
from lxml import etree
import csv
import time

headers = {
    'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 83.0.4103.106Safari / 537.36'
}
f = open('qfang.csv', 'a', encoding='utf-8')  # 追加方式创建并打开文件 qfang.csv
f.write('名称，板块，均价\n')  # 第一行写入标题名称，板块，均价
for x in range(1, 5):  # 这里以前 4 页为例，循环采集前 4 个页面
    url = 'https://nanjing.qfang.com/newhouse/list/n'
    url = url + str(x)  # 分析页面，发现页面的变化规律
    html = requests.get(url, headers=headers)
    time.sleep(1)
    selector = etree.HTML(html.text)
    xiaoqulist = selector.xpath('/html/body/div[4]/div/div[1]/div[4]/ul/li')
    for xiaoqu in xiaoqulist:
        try:
            mc = xiaoqu.xpath('div[2]/div[1]/a/em/text()')[0]  # 小区名称
            bk = xiaoqu.xpath('div[2]/div[2]/p[1]/text()')[0]  # 小区板块
            jj = xiaoqu.xpath('div[3]/p[1]/span[1]/text()')[0]  # 小区均价
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
