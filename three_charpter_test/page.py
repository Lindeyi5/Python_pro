# # # # 开发时间：2023-04-10 17:13
# # # # 开发人员：林坚洪
# # # # encodeing "UTF-8"
# # # # 好的，下面是一个简单的Python代码，可以批量爬取网易云音乐的歌曲信息：
# # # #
# # # # ```python
# # # import requests
# # # import json
# # #
# # # # 设置请求头
# # # headers = {
# # #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# # #
# # # # 输入要爬取的歌单id
# # # playlist_id = input("请输入要爬取的歌单id:")
# # #
# # # # 构造url
# # # url = 'https://music.163.com/api/playlist/detail?id=' + playlist_id
# # #
# # # # 发送请求
# # # response = requests.get(url, headers=headers)
# # #
# # # # 解析响应
# # # data = json.loads(response.text)
# # # tracks = data['result']['tracks']
# # #
# # # # 遍历歌曲信息
# # # for track in tracks:
# # #     print('歌曲名称：', track['name'])
# # #     print('歌手名称：', track['artists'][0]['name'])
# # #     print('专辑名称：', track['album']['name'])
# # #     print('歌曲时长：', track['duration'], 'ms')
# # #     print('歌曲链接：', 'https://music.163.com/#/song?id=' + track['id'])
# # #     print('----------------------------------------------')
# # # # ```
# # # #
# # # # 具体步骤如下：
# # # #
# # # # 1. 导入requests和json模块
# # # # 2. 构造请求头
# # # # 3. 输入要爬取的歌单id
# # # # 4. 构造url
# # # # 5. 发送请求
# # # # 6. 解析响应，获取歌曲信息
# # # # 7. 遍历歌曲信息，输出想要的信息
# # # #
# # # # 注意：该代码需要在能够访问网易云音乐的网络环境下运行。
# # # #
# # # # 您今天还有 4 次免费提问｜19.5s
# # # !/usr/bin/python
# # # -*- coding: utf-8 -*-
# # # @Time    : 2020/4/24 15:05
# # # @Author  : zh
# # # @File    : wangyiyun.py
# # import json
# # import os
# # import re
# # from pprint import pprint
# #
# # import requests
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# #
# #
# # class WangYiYun():
# #     def __init__(self):
# #         self.song_mp3_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'
# #         self.song_list_id = 'https://music.163.com/#/playlist?id={}'
# #         self.headers = {
# #             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
# #         }
# #         self.song_url = "https://music.163.com/#/search/m/?s={}&type=1"
# #         self.songs = []
# #
# #     def show_menu(self):
# #         print("欢迎来到网易云音乐下载中心")
# #         print("-" * 50)
# #         print("1. 下载单曲")
# #         print("2. 下载歌单")
# #         print("3. 退出")
# #         print("-" * 50)
# #
# #     def run(self):
# #         self.show_menu()
# #         while True:
# #             option = int(input("请输入您要进行的操作:"))
# #             if option not in [1, 2, 3]:
# #                 print("请重新输入")
# #             if option == 1:
# #                 song_name = input("请输入歌曲名称:")
# #                 song_id = self.get_song_id(song_name)
# #             if option == 2:
# #                 # 下载歌单
# #                 menu_id = int(input("请输入您要下载的歌单id："))
# #                 list_id = self.get_song_list_id(menu_id)
# #             else:
# #                 break
# #
# #     def get_song_list_id(self, nmenu_id):
# #         option = webdriver.ChromeOptions()
# #         option.add_argument('--headless')
# #         driver = webdriver.Chrome(r'chromedriver.exe',
# #                                   chrome_options=option)
# #         driver.get(self.song_list_id.format(nmenu_id))
# #         driver.switch_to.frame('g_iframe')
# #         # wd.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div[1]/div[1]/div/ul/li[2]/a')
# #
# #         # list_name = driver.find_element(By.XPATH,('//div[@class="tit"]/h2').text
# #         list_name = driver.find_element(By.XPATH, '//div[@class="tit"]/h2').text
# #         list_name = "".join(list_name.split())
# #         list_name = re.sub(r'\W', '', list_name)
# #         if not os.path.exists(list_name):
# #             os.mkdir(list_name)
# #         a_list = driver.find_elements(By.XPATH,'//span[@class="txt"]/a')
# #         title_list = driver.find_elements(By.XPATH,'//span[@class="txt"]/a/b')
# #
# #         for a in a_list:
# #             item = {}
# #             item["song_id"] = a.get_attribute('href').split("=")[-1]
# #             item["song_name"] = title_list[a_list.index(a)].get_attribute('title').replace(u'\xa0', u'')
# #             item["song_name"] = item["song_name"].replace(u'\xf1', u'')
# #             self.songs.append(item)
# #
# #         for item in self.songs:
# #             self.download_song(item, list_name)
# #
# #     def get_song_id(self, song_name):
# #         option = webdriver.ChromeOptions()
# #         option.add_argument('--headless')
# #         driver = webdriver.Chrome(r'C:\Users\zh\Desktop\jxsz_code\pachong_code\chromedriver.exe',
# #                                   chrome_options=option)
# #         driver.get(self.song_url.format(song_name))
# #         driver.switch_to.frame('g_iframe')
# #         song_url = driver.find_element(By.XPATH,"//div[@class='text']/a").get_attribute('href')
# #         item = {}
# #         item["song_id"] = song_url.split('=')[-1]
# #         item["song_name"] = driver.find_element(By.XPATH,"//div[@class='text']/a/b").get_attribute('title')
# #         self.download_song(item)
# #         driver.close()  # 退出当前页面
# #         driver.quit()  # 退出浏览器
# #
# #     def download_song(self, item, dir_name=None):
# #         req = requests.get(self.song_mp3_url.format(item["song_id"]), headers=self.headers)
# #         if dir_name is None:
# #             with open('%s.mp3' % item["song_name"], 'wb') as f:
# #                 f.write(req.content)
# #         else:
# #             try:
# #                 with open('%s/%s.mp3' % (dir_name, item["song_name"]), 'wb') as f:
# #                     # with open('%s.mp3' % item["song_name"], 'wb') as f:
# #                     f.write(req.content)
# #                     print(item["song_id"])
# #                 print("%s 下载完成" % item["song_name"])
# #             except:
# #                 pass
# #
# #     def test(self):
# #         req = requests.get(self.song_mp3_url.format(1439803847), headers=self.headers)
# #         # print(req.headers)
# #         with open("a.mp3", "wb") as f:
# #             f.write(req.content)
# #
# #
# # wangyiyun = WangYiYun()
# # wangyiyun.run()
# import requests, os, time, sys, re
# from urllib import request
# import Selector
#
#
# class wangyiyun():
#     def __init__(self):
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
#             'Referer': 'http://music.163.com/'}
#         self.main_url = 'https://music.163.com/'
#         self.session = requests.Session()
#         self.session.headers = self.headers
#
#     def get_songurls(self, playlist):
#         '''进入所选歌单页面，得出歌单里每首歌各自的ID 形式就是“song?id=64006"'''
#         url = self.main_url + 'playlist?id=%d' % playlist
#         re = self.session.get(url)  # 直接用session进入网页，懒得构造了
#         sel = Selector(text=re.text)  # 用scrapy的Selector，懒得用BS4了
#         songurls = sel.xpath('//ul[@class="f-hide"]/li/a/@href').extract()
#         return songurls  # 所有歌曲组成的list
#         ##['/song?id=64006', '/song?id=63959', '/song?id=25642714', '/song?id=63914', '/song?id=4878122', '/song?id=63650']
#
#     def get_songinfo(self, songurl):
#         '''根据songid进入每首歌信息的网址，得到歌曲的信息
#         return：'64006'，'陈小春-失恋王'''
#         url = self.main_url + songurl
#         re = self.session.get(url)
#         sel = Selector(text=re.text)
#         song_id = url.split('=')[1]
#         song_name = sel.xpath("//em[@class='f-ff2']/text()").extract_first()
#         singer = '&'.join(sel.xpath("//p[@class='des s-fc4']/span/a/text()").extract())
#         songname = singer + '-' + song_name
#         return str(song_id), songname
#
#     def download_song(self, songurl, dir_path):
#         '''根据歌曲url，下载mp3文件'''
#         song_id, songname = self.get_songinfo(songurl)  # 根据歌曲url得出ID、歌名
#         song_url = 'http://music.163.com/song/media/outer/url?id=%s.mp3' % song_id
#         path = dir_path + os.sep + songname + '.mp3'  # 文件路径
#         request.urlretrieve(song_url, path)  # 下载文件
#
#     def work(self, playlist):
#         songurls = self.get_songurls(playlist)  # 输入歌单编号，得到歌单所有歌曲的url
#         dir_path = r'C:\Users\HP\Desktop\Music'
#         for songurl in songurls:
#             self.download_song(songurl, dir_path)  # 下载歌曲
#
#
# if __name__ == '__main__':
#     d = wangyiyun()
#     d.work(2895575219)
#     # ```
'https://m801.music.126.net/20230410175859/2b1b05bf91f7f4fba95f5467da215337/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/26005659253/3d04/b32d/32fc/e39ece6a8b0cc79a3125449042145b44.m4a'

'https://m701.music.126.net/20230410175926/afb8fd0872fa937e39a2cb70d64f31bb/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/25815392008/c627/81a7/8197/d1c587540f423beef4a03af8a19ad851.m4a'