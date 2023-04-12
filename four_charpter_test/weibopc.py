# 开发时间：2023-03-29 10:40
# 开发人员：林坚洪
# encodeing "UTF-8"
import json
import re
import requests
from lxml import etree
import csv
import time
import keyword


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cookie': 'UOR=www.baidu.com,weibo.com,www.baidu.com; SINAGLOBAL=5185269950651.649.1674560956619; PC_TOKEN=79ef9367e3; XSRF-TOKEN=_VsVpFkItPJYieiOFX8ZKKBH; _s_tentry=weibo.com; Apache=1076035566898.5677.1680055564611; ULV=1680055564670:2:1:1:1076035566898.5677.1680055564611:1675584755347; login_sid_t=ada457e4fc9b76e38c82dd85487a0a53; cross_origin_proto=SSL; wb_view_log=1536*8641.25; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF0DOaM-c0SqK7BIq6my7gB5JpX5o275NHD95QNSKe0ShB7eK2XWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0-0e0BXeh2pS5tt; SSOLoginState=1680055675; SUB=_2A25JJ-0sDeRhGeFL6FEV9C7NyjiIHXVqVVnkrDV8PUNbmtANLXPCkW9NQjuS5mkOf7c3ohrxHY-mhVbd_utMz-5X; ALF=1711591675; WBPSESS=-dKfHVSD-hoYfzB5RQHAgNOgHx4nTgIWGGQW7cXME6K7OF2fiYU6AxyI5LrmC_IAbH5dNlcSRUNNA6LCla4OBKciABabNhjkOdINgBc85yOyU1ofFmTIpt_HVYUBPKULAR2uNtTCX88KMWlJZH0XPg==',
    'referer': ''
}
url = 'https://weibo.com/2028810631/Mzoi1BGUZ'
url2 = 'https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id=4884348538983117&is_show_bulletin=2&is_mix=0&max_id=192742784020543&count=20&uid=2028810631&fetch_level=0'
url3 = 'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4884348538983117&is_show_bulletin=2&is_mix=0&count=10&uid=2028810631&fetch_level=0'
htm = requests.get(url3)
# print(htm.status_code)
data = htm.json()
# data = htm.strip('\n')
# data = json.loads(htm)
# print(data)
data1 = data['max_id']
print(data1)
# data2 = data['ok']
data2 = data['total_number']
for i in range(0, 19):
    if (exit(data['data'][i]['source'])):
        data3 = data['data'][i]['source']
    else:
        data3 = '未知地址'
    'text_raw'
    data4 = data['data'][i]['text_raw']
    print(data3, data4, end='\n')
#
# f = open('taobaoxinxi.csv', 'w', encoding='utf-8')
#
# f.write('视频标题，up主，播放次数，弹幕数量，描述\n')
# from bs4 import BeautifulSoup
#
# for item in data:
#     temp = {
#         'title': BeautifulSoup(item['title'], 'html.parser').get_text(),
#         'view_price': item['view_price'],
#         'view_sales': re.sub('[^0-9]', '', item['view_sales']),
#         'view_fee': '是' if item['view_fee'] == '0.00' else '否',
#         'isTmall': '是' if item['shopcard']['isTmall'] else '否',
#         'area': item['item_loc']}
#     f.write('{title},{view_price},{view_sales},{view_sales},{view_fee},{isTmall},{area}\n'.format(**temp))
# f.close()

'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4884348538983117&is_show_bulletin=2&is_mix=0&count=10&uid=2028810631&fetch_level=0'
'https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id=4884348538983117&is_show_bulletin=2&is_mix=0&max_id=192742784020543&count=20&uid=2028810631&fetch_level=0'
'https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id=4884348538983117&is_show_bulletin=2&is_mix=0&max_id=145188911391739&count=20&uid=2028810631&fetch_level=0'
