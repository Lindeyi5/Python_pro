# 开发时间：2023-03-15 11:15
# 开发人员：林坚洪
# encodeing "UTF-8"
import requests
from lxml import etree

htm = '''
 <html>
 <div>
 <ul>
 <li class="item-0"><a href="src/1.html">第一个项目</a></li>
 <li class="item-1"><a href="src/2.html">第二个项目</a></li>
 <li class="item-2"><a href="src/3.html">第三个项目</a></li>
 <li class="item-1"><a href="src/4.html">第四个项目</a></li>
 <li class="else-0"><a href="src/5.html">其它项目</a></li>
 ul 里的文本
 </ul>
 </div>
 </html>
'''
# print(htm)
selector = etree.HTML(htm)  # 将 htm 文本传入 etree 的 HTML 解析功能，返回选择器
all_li = selector.xpath('//div/ul/li')  # 选择器的 xpath 对节点元素进行访问，返回列表
print(all_li)

li_1 = selector.xpath('//div/ul/li[1]/a/text()')  # 访问第一个 li 元素，注意下标从 1 开始
print(li_1)

print(li_1[0])

li_3 = selector.xpath('//*[@class="item-1"]/a/text()')
print(li_3)

link_1 = selector.xpath('//li/a/@href')
print(link_1)

all_text=selector.xpath('//li/a/text()')
print(all_text)

all_text = ''
all_li = selector.xpath('//div/ul/li ')
for c in all_li:
    all_text = all_text + c.xpath('a/text()')[0] + " "
print(all_text)

all_text = []
all_li = selector.xpath('//li[starts-with(@class,"item-")]')
for c in all_li:
    all_text.append(c.xpath('a/text()')[0])
print(all_text)

all_text = selector.xpath('//ul/text()')
print(all_text)

all_clean = []
for c in all_text:
    if c.strip():
        all_clean.append(c.strip())
print('21',all_clean)

all_text = selector.xpath('string(//ul)')
print(all_text)

all_text = all_text.strip().replace(' ', '').replace('\n', ' ')
print(all_text)

