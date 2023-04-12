# 开发时间：2023-03-24 17:47
# 开发人员：林坚洪
# encodeing "UTF-8"
import requests
from lxml import etree
import re

headers = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}
import requests
def music_search():
    name = input("请输入要搜索的内容:")
    url = 'https://musicapi.leanapp.cn/search?keywords='+name
    id_list = requests.get(url=url).json()
    ids = []
    names = []
    for id in id_list['result']['songs']:
        ids.append(id['id'])
        names.append(id['name'])
    music_dict = dict(zip(names, ids))
    print('\n')
    for key,value in music_dict.items():
        print(key,"的id为",value)
    print('\n')
def music_download():
    id_choice=input('请选择要下载的歌曲id:')
    id_choice=id_choice.replace(' ', '')
    url='http://music.163.com/song/media/outer/url?id='+id_choice+'.mp3'
    headers={
        'User-Agent': 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Referer': 'https://email.163.com/'
    }
    music_data=requests.get(url=url,headers=headers).content
    name=input('请为该歌曲命名:')+'.mp3'
    print('正在下载中')
    fp=open(name,'wb')
    fp.write(music_data)
    print(name,'下载成功')

if __name__=='__main__':
    music_search()

    music_download()
    choice=input('请选择接下来的操作重新搜索(1) 继续下载(2) 退出(任意)')
    while True:
        if choice==1:
            music_search()
        elif choice==2:
            music_download()
        else:
            break



