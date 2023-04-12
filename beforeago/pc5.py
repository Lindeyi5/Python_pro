# 开发时间：2023-01-18 22:02
# 开发人员：林坚洪
import requests
import parsel
#,verify=False
'''filename = 'image\\'
if not os.path.exists(filename):
    os.mkdir(filename)'''
k=13
i = (k-1)*24+1
for page in range(k, 15):
    print(f'========正在爬取第{page}页========')
    url = f'https://wallhaven.cc/search?categories=111&purity=010&topRange=1M&sorting=toplist&order=desc&page={page}'
    headers = {
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / '
                        '108.0.0.0Safari / 537.36Edg / 108.0.1462.54 '
    }
    response = requests.get(url, headers=headers,verify=False)
    # html=response.text
    # print(html)
    selector = parsel.Selector(response.text)
    # href = selector.css('.thumb-listing-page ul li a::attr(href)').getall()
    # print(href)
    lis = selector.css('.thumb-listing-page ul li')
    for li in lis:
        # title = li.css()
        lis_url = li.css('a::attr(href)').get()
        # print(lis_url)
        # title = li.css('href::text').get()
        # if title:
        response_2 = requests.get(url=lis_url, headers=headers,verify=False)
        selector_2 = parsel.Selector(response_2.text)
        title = selector_2.css('.scrollbox img::attr(alt)').get()
        img_url = selector_2.css('.scrollbox img::attr(src)').get()
        img_content = requests.get(url=img_url).content
        with open('image\\' + str(i) + '.jpg', mode='wb') as f:
            f.write(img_content)
            print(title, img_url)
        i += 1

    # urls = re.findall('<a class="(.*?)" href="(.*?)" target="(.*?)">',html)
    # print(urls)
    # <a class="preview" href="https://wallhaven.cc/w/p99l1e"  target="_blank"  ></a>'''
