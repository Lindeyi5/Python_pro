# 开发时间：2023-03-15 11:15
# 开发人员：林坚洪
# encodeing "UTF-8"
import requests
from lxml import etree

url = 'https://www.baidu.com'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
htm = requests.get(url, headers=headers)
htm.encoding = 'utf-8'

selector = etree.HTML(htm.text)  # 将 htm 文本传入 etree 的 HTML 解析功能，返回选择器
num1 = selector.xpath('//*[@class="title-content-title"]/text()')
print(num1)
num2 = selector.xpath('//*[@class="s-hotsearch-content"]/li/a/@href')
print(num2)
num3 = selector.xpath('//*[@id="hotsearch-content-wrapper"]/li/a/@href')
print(num3)
num4 = selector.xpath('//*[@id="s_lg_img_new"]/@src')
print(num4)
num5 = 'https:' + num4[0];
print(num5)
t = requests.get(num5)
with open('baidu.jpg', 'wb') as f:
    f.write(t.content)
