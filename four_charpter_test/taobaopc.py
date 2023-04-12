# 开发时间：2023-03-27 10:34
# 开发人员：林坚洪
# encodeing "UTF-8"
'/html/body/div[1]/div[2]/div[3]/div[1]/div[21]/div/div/div[1]/div[1]/div[1]/div/div[1]/a/img'
# 开发时间：2023-03-21 19:24
# 开发人员：林坚洪
# encodeing "UTF-8"

import re
import json

with open('taobao.txt', 'r', encoding='utf-8') as fp:
    data = fp.read()
data = data.strip('\n')
data = json.loads(data)
data = data['mods']['itemlist']['data']['auctions']
print(data)

f = open('taobaoxinxi.csv', 'w', encoding='utf-8')

f.write('视频标题，up主，播放次数，弹幕数量，描述\n')
from bs4 import BeautifulSoup

for item in data:
    temp = {
        'title': BeautifulSoup(item['title'], 'html.parser').get_text(),
        'view_price': item['view_price'],
        'view_sales': re.sub('[^0-9]', '', item['view_sales']),
        'view_fee': '是' if item['view_fee'] == '0.00' else '否',
        'isTmall': '是' if item['shopcard']['isTmall'] else '否',
        'area': item['item_loc']}
    f.write('{title},{view_price},{view_sales},{view_sales},{view_fee},{isTmall},{area}\n'.format(**temp))
f.close()
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
# }
# headers1 = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
#     'Connection': 'keep-alive',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Cookie': 'cookies',
#     'referer': ''
# }
#
# f = open('taobao.csv', 'a', encoding='utf-8')
# # f.write('电影名，主演，上映时间，评分\n')
#
# for i in range(1, 5):
#     url = 'https://s.taobao.com/search?q=Python&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306'
#     str1 = '&offset=' + str((i - 1) * 10) + ''
#     # url = url + str1
#     print(url)
#     htm = requests.get(url, headers=headers)
#     print(htm.text)
#     htm.encoding = 'utf-8'
#     selector = etree.HTML(htm.text)
#     dianyinlist = selector.xpath('/html/body/div[4]/div/div/div[1]/dl/dd')
#     for dianyin in dianyinlist:
#         try:
#             mz = dianyin.xpath('div/div/div[1]/p[1]/a/text()')[0]  # 电影名字
#             zy = dianyin.xpath('div/div/div[1]/p[2]/text()')[0]
#             sysj = dianyin.xpath('div/div/div[1]/p[3]/text()')[0]
#             pf1 = dianyin.xpath('div/div/div[2]/p/i[1]/text()')[0]
#             pf2 = dianyin.xpath('div/div/div[2]/p/i[2]/text()')[0]
#             pf = str(pf1) + str(pf2)
#             mz=str(mz.strip().replace('\r', '').replace('\n', '').replace(' ', ''))
#             zy=str(zy.strip().replace('\r', '').replace('\n', '').replace(' ', ''))
#             sysj=str(sysj.strip().replace('\r', '').replace('\n', '').replace(' ', ''))
#             pf=str(pf.strip().replace('\r', '').replace('\n', '').replace(' ', ''))
#         except:
#             continue
#         temp = {
#             'mingchen': mz,
#             'zhuyan': zy,
#             'shangyinshijian': sysj,
#             'pinfen': pf
#         }
#         try:
#             f.write('{mingchen},{zhuyan},{shangyinshijian},{pinfen}\n'.format(**temp))  # 写入文件
#         except:
#             print('写入错误！')
#         print('正在抓取：', mz)
