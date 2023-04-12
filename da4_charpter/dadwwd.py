# 开发时间：2023-03-15 10:28
# 开发人员：林坚洪
# encodeing "UTF-8"
# 开发时间：2023-03-13 11:37
# 开发人员：林坚洪
# encodeing "UTF-8"
import requests
from lxml import etree
from lxml import html

etree = html.etree
htm = '''
    < html >
        < div >
            < ul >
                < li class ="item-0" > < a href="src/1.html" > 第一个项目 < / a > < / li >
                < li class ="item-1" > < a href="src/2.html" > 第二个项目 < / a > < / li >
                < li class ="item-2" > < a href="src/3.html" > 第三个项目 < / a > < / li >
                < li class ="item-1" > < a href="src/4.html" > 第四个项目 < / a > < / li >               
                < li class ="else-0" > < a href="src/5.html" > 其它项目 < / a > < / li >
                ul里的文本
            < / ul >
        < / div >
    < / html >
'''
selector = etree.HTML(htm)
all_li = selector.xpath('/div/ul/li')
print(all_li)
