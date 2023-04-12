# 开发时间：2023-03-27 10:26
# 开发人员：林坚洪
# encodeing "UTF-8"
import requests
from lxml import etree
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
# from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

# from config import logger_config
from selenium import webdriver

from selenium import webdriver

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('headless')

# 打开chrome浏览器

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

# brower = webdriver.Chrome()
# proxy_addr = {'http': "202.75.210.45:7777"}
'https://www.gaokao.cn/'
browser.get('https://s.taobao.com/search?q=Python&suggest=history_1&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&_input_charset=utf-8&wq=&suggest_query=&source=suggest')
time.sleep(10)
# brower.get('https://www.gaokao.cn/school/search')
print(browser.page_source)
# cookied = '__wpkreporterwid_=1b5e7fa1-e0d1-42cc-a3eb-e3fedc302cf4; gr_user_id=a3241ab3-31d1-4dec-8bad-ae3ae90f8010; UM_distinctid=18720e609069e4-0673f2fb1b0f7d-26031851-144000-18720e60907188e; 88025341dda01c5f_gr_session_id=7cfb8db3-e3f0-4d13-8dae-1e086dce351c; 88025341dda01c5f_gr_session_id_7cfb8db3-e3f0-4d13-8dae-1e086dce351c=true; Hm_lvt_17c8dee9c87e3ab669ce5dd4f88140ec=1679884159,1679902300; Hm_lpvt_17c8dee9c87e3ab669ce5dd4f88140ec=1679902300; Hm_lvt_9b4517aa97b6b67e7c396bef15886cef=1679884159,1679902300; Hm_lpvt_9b4517aa97b6b67e7c396bef15886cef=1679902300; Hm_lvt_5ef3ea976e817c8d0be475b561b35e99=1679884159,1679902300; Hm_lpvt_5ef3ea976e817c8d0be475b561b35e99=1679902300; areaid=31; cityid=3101; CNZZDATA4696252=cnzz_eid%3D1388065715-1679881228-%26ntime%3D1679900729',

headers = {
    'cookies': '__wpkreporterwid_=1b5e7fa1-e0d1-42cc-a3eb-e3fedc302cf4; gr_user_id=a3241ab3-31d1-4dec-8bad-ae3ae90f8010; UM_distinctid=18720e609069e4-0673f2fb1b0f7d-26031851-144000-18720e60907188e; 88025341dda01c5f_gr_session_id=7cfb8db3-e3f0-4d13-8dae-1e086dce351c; 88025341dda01c5f_gr_session_id_7cfb8db3-e3f0-4d13-8dae-1e086dce351c=true; Hm_lvt_17c8dee9c87e3ab669ce5dd4f88140ec=1679884159,1679902300; Hm_lpvt_17c8dee9c87e3ab669ce5dd4f88140ec=1679902300; Hm_lvt_9b4517aa97b6b67e7c396bef15886cef=1679884159,1679902300; Hm_lpvt_9b4517aa97b6b67e7c396bef15886cef=1679902300; Hm_lvt_5ef3ea976e817c8d0be475b561b35e99=1679884159,1679902300; Hm_lpvt_5ef3ea976e817c8d0be475b561b35e99=1679902300; areaid=31; cityid=3101; CNZZDATA4696252=cnzz_eid%3D1388065715-1679881228-%26ntime%3D1679900729',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}
'''def use_proxy(proxy_addr,url):
    import urllib.request
    proxy=urllib.request.ProxyHandler({'http':proxy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode('utf-8')
    return data
proxy_addr="202.75.210.45:7777"
data=use_proxy(proxy_addr,"http://www.baidu.com")
print(len(data))'''
# loc = (By.ID, "root")
# EC.visibility_of_element_located(loc)  # 等待元素可见的条件
# until 直到什么什么
# print(brower.page_source)
# WebDriverWait(brower, 10, 0.5).until(EC.visibility_of_element_located(loc))

# brower.implicitly_wait(5)

# brower.quit()
# get_content = driver.find_element(By.TAG_NAME, "app-home").text
# brower.execute_script()

# brower.close()
# html = requests.get('https://www.gaokao.cn/school/search', headers=headers,)
# html.encoding = 'utf-8'
# print(html.content)


# selector = etree.HTML(brower.page_source)
# print(selector)
# f = open('gaokao.csv', 'a', encoding='utf-8')
# f.write('院校名称,学校类别,所属地区\n')
# '/html/body/div/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[2]/div[1]/a/span[1]'
# schoollist = selector.xpath('//*[@id="myTable"]/tbody')
# # schoollist=selector.xpath('/html/body/div/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[2]/div[1]/a/span[1]')
# print(schoollist)

# i=1
# for school in schoollist:
#     try:
#         name=school.xpath('tr['+str(i)+']/td[2]/div[1]/a/span[1]/text()')
#         print(name)
#         type=school.xpath('tr['+str(i)+']/td[2]/div[2]/span[2]/text()')
#         print(type)
#         area=school.xpath('tr['+str(i)+']/td[2]/div[1]/a/span[2]/text()')
#         print(area)
#         i=i+1
#     except:
#         continue
# f.close()
