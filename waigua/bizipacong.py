# 开发时间： 2022/7/29  22:25
# 开发人：林坚洪
import requests #用于请求网页
import re  #正则表达式，用于解析筛选网页中的信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }
response = requests.get('https://www.4kbizhi.com/', headers=headers)