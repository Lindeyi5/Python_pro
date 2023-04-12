# 开发时间：2023-03-16 10:12
# 开发人员：林坚洪
# encodeing "UTF-8"
import requests
from lxml import etree

url = 'https://movie.douban.com/subject/35267208/comments?limit=20&status=P&sort=new_score'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
htm = requests.get(url, headers=headers)
htm.encoding = 'utf-8'
# print(r.status_code)
# print(htm.text)
# print(r.content)

selector = etree.HTML(htm.text)  # 将 htm 文本传入 etree 的 HTML 解析功能，返回选择器
short = selector.xpath('//*[@class="short"]/text()')
# short_content = selector.xpath('//*[@class="short_content"]/text()') # 选择器的 xpath 对节点元素进行访问，返回列表
print(short)
all_short=''
# for i in short:
#     all_short=all_short+i.xpath('//*[@class="short"]/text()')[0]+' '
# print(all_short)

