# 开发时间：2023-04-14 12:39
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

url_1 = 'https://api.bilibili.com/x/v2/reply/reply?csrf=a4477cd59d624bce7e24f62796d76ab0&oid=752825895&pn=3&ps=10&root=2742652493&type=1'
url_2 = 'https://api.bilibili.com/x/v2/reply/main?csrf=a4477cd59d624bce7e24f62796d76ab0&mode=3&next=0&oid=752825895&plat=1&seek_rpid=&type=1'

url_3 = 'https://api.bilibili.com/x/v2/reply/main?csrf=a4477cd59d624bce7e24f62796d76ab0&mode=3&next=2&oid=752825895&plat=1&type=1'


def crawling_comments(dat):
    htm = requests.get(url)
    data = htm.json()
    data1 = data['data']['root']['content']['message']  # 查找评论原文
    return data1


def crawling_replies(dat):
    htm = requests.get(url)
    data = htm.json()
    kk = []
    for i in range(0, 20):
        data[i] = data['data']['replies'][i]['content']['message']  # 查找评论回复原文
        kk.append(data[i])
    return kk


def data_cleaning(array):
    ar = ' '.join(array)  # 字符串拼接
    # arr2 = re.sub(r'[^\u4e00-\u9fa5]', '', ar, count=0, flags=0)
    # sentence = re.sub(r'[A-Za-z0-9_.!+-=——,$%^，。？、~@#￥%……&*《》<>「」{}\[\.\*\]【】()/]', '', ar)
    sentence = re.sub(r'["”‘“]', '', ar)
    sentence2 = sentence.replace('\n\t',' ').replace('\n',' ')
    # arr2 = re.sub(r'[^\u4e00-\u9fa5]', '', ar, count=0, flags=0)
    return sentence2


# print(s)
# # 爬取评论的回复
for i in range(1, 4):
    url = 'https://api.bilibili.com/x/v2/reply/main?csrf=a4477cd59d624bce7e24f62796d76ab0&mode=3&next='+str(i)+'&oid=752825895&plat=1&type=1'
    # s = crawling_comments(url)
    s1 = crawling_replies(url)
    s11 = data_cleaning(s1)
    print(s11)

# print(s)

# data = htm.strip('\n')
# data = json.loads(htm)
# print(data)


# data2 = data['data']['replies'][0]['content']['message']  # 查找评论回复原文

# print(data2)
# data2 = data['ok']

# data2 = data['total_number']
# for i in range(0, 19):
#     if (exit(data['data'][i]['source'])):
#         data3 = data['data'][i]['source']
#     else:
#         data3 = '未知地址'
#     'text_raw'
#     data4 = data['data'][i]['text_raw']
#     print(data3, data4, end='\n')
