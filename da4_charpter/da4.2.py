# 开发时间：2023-03-13 11:01
# 开发人员：林坚洪
# encodeing "UTF-8"
import requests
url = 'https://www.douban.com/search'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
dicts = {
    'q': 'python',
    'cat':'1001'
}
r = requests.get(url, headers=headers, params=dicts)

r.encoding = 'utf-8'
print(r.status_code)
print(r.text)
# print(r.content)