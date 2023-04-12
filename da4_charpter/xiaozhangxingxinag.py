# 开发时间：2023-03-20 10:38
# 开发人员：林坚洪
# encodeing "UTF-8"
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

f = open('xinxiang.csv', 'a', encoding='utf-8')
f.write('查询码，标题，提交时间，处理状态\n')

for i in range(1, 5):
    url = 'http://www.xiyi.edu.cn/gzcylist.jsp?totalpage=101&PAGENUM=' + str(
        i) + '&urltype=tree.TreeTempUrl&wbtreeid=1172'
    htm = requests.get(url, headers=headers)
    # print(htm.text)
    # time.sleep(1)
    htm.encoding = 'utf-8'
    selector = etree.HTML(htm.text)
    # '/html/body/div[6]/div[1]/div[3]/table[1]/tbody/tr[6]/td[3]/a'
    '/html/body/div[6]/div[1]/div[3]/table[1]/tbody/tr[3]/td[3]/a'
    xiaoqulist = selector.xpath('/html/body/div[6]/div[1]/div[3]/table[1]//tr/td/a/text()')[0]
    print(xiaoqulist)
        #         bt = xiaoqu.xpath('/tr/td[3]/text()')[0]
        #         sj = xiaoqu.xpath('/tr/td[4]/text()')[0]
        #         clzt = xiaoqu.xpath('/tr/td[5]/text()')[0]
        #         print(cxm)

    #     temp = {
    #         'mingchen': cxm,
    #         'bankuai': bt,
    #         'junjia': sj,
    #         'caxunzhuangtai': clzt
    #     }
    #     try:
    #         f.write('{mingchen},{bankuai},{junjia},{caxunzhuangtai}\n'.format(**temp))  # 写入文件
    #     except:
    #         print('写入错误！')
    #     print('正在抓取：', bt)
