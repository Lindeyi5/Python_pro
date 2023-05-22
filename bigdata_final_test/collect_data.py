# 开发时间：2023-05-11 10:40
# 开发人员：林坚洪
# encodeing "UTF-8"
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cookie': 'UOR=www.baidu.com,weibo.com,www.baidu.com; SINAGLOBAL=5185269950651.649.1674560956619; PC_TOKEN=79ef9367e3; XSRF-TOKEN=_VsVpFkItPJYieiOFX8ZKKBH; _s_tentry=weibo.com; Apache=1076035566898.5677.1680055564611; ULV=1680055564670:2:1:1:1076035566898.5677.1680055564611:1675584755347; login_sid_t=ada457e4fc9b76e38c82dd85487a0a53; cross_origin_proto=SSL; wb_view_log=1536*8641.25; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF0DOaM-c0SqK7BIq6my7gB5JpX5o275NHD95QNSKe0ShB7eK2XWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0-0e0BXeh2pS5tt; SSOLoginState=1680055675; SUB=_2A25JJ-0sDeRhGeFL6FEV9C7NyjiIHXVqVVnkrDV8PUNbmtANLXPCkW9NQjuS5mkOf7c3ohrxHY-mhVbd_utMz-5X; ALF=1711591675; WBPSESS=-dKfHVSD-hoYfzB5RQHAgNOgHx4nTgIWGGQW7cXME6K7OF2fiYU6AxyI5LrmC_IAbH5dNlcSRUNNA6LCla4OBKciABabNhjkOdINgBc85yOyU1ofFmTIpt_HVYUBPKULAR2uNtTCX88KMWlJZH0XPg==',
    'referer': ''
}
url = 'https://s.weibo.com/weibo?q=python&Refer=SWeibo_box'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
weibo_list = soup.find_all('div', class_='content')

for weibo in weibo_list:
    print(weibo.text)
