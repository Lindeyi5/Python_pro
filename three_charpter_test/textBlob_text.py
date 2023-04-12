# # 开发时间：2023-04-10 10:29
# # 开发人员：林坚洪
# # encodeing "UTF-8"
# from textblob import TextBlob
#
# # tb = TextBlob("TextBlob aims to provide access to common text-processing operations through a familiar interface.")
# # # print(tb.tags)
# # # print(tb)
# # print(tb.noun_phrases)
# # print(tb.words)
# # animals = TextBlob("apple,elephant,octopus,peach!")
# # print(animals.words)
# # print(animals.words.pluralize())
#
# testimonial = TextBlob("Python is an amazing programming language. It's very bad and good and bad and bad!")
# print(testimonial.sentiment)
# print(round(testimonial.sentiment.polarity, 2))  # 0.8
# print(testimonial.sentiment.subjectivity)  # 0.84
# # adddd=TextBlob("we can go to school togather happily and said!")
# # print(adddd.sentiment)
# zen = TextBlob("Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.")
# print(zen.words)
# print(zen.sentences)
#
# x = TextBlob("I am a good student. I try to study python!")
# print(x.words)
# print(x.sentences)
# print(x.sentiment)
# for i in x.sentences:
#     print(i.sentiment)
#
# for sentence in zen.sentences:
#     print(sentence.sentiment)
#
# hello = TextBlob("We are saying hello to you.We are now saying hello, hello, HELLO to you.")
# print(hello.word_counts['hello'])
#
# print(hello.words.count('hello', case_sensitive=True))
#
# blob = TextBlob("What you say is very funny.")
# print(blob.ngrams(n=3))
# print(blob.ngrams(n=2))
#
# from textblob.classifiers import NaiveBayesClassifier
#
# train = [
#     ('I love this sandwich.', 'pos'),
#     ('this is an amazing place!', 'pos'),
#     ('I feel very good about these beers.', 'pos'),
#     ('this is my best work.', 'pos'),
#     ("what an awesome view", 'pos'),
#     ('I do not like this restaurant', 'neg'),
#     ('I am tired of this stuff.', 'neg'),
#     ("I can't deal with this", 'neg'),
#     ('he is my sworn enemy!', 'neg'),
#     ('my boss is horrible.', 'neg')
# ]
# cl = NaiveBayesClassifier(train)
# print(cl)
# result = cl.classify("This is an amazing library!")
# print(result)
#
# prob_dist = cl.prob_classify("you do not like me.")  # 预测概率分布
# print(prob_dist.max())  # 最终结果 neg
# print(round(prob_dist.prob("pos"), 2))  # 预测是 pos 的概率
# print(round(prob_dist.prob("neg"), 2))
#
# blob = TextBlob("The beer is good. But the hangover is horrible.", classifier=cl)
# print(blob.classify())
#
# for s in blob.sentences:
#     print(s.classify())
import requests, os, time, sys, re
from urllib import request
from scrapy.selector import Selector


class wangyiyun():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Referer': 'http://music.163.com/'}
        self.main_url = 'https://music.163.com/'
        self.session = requests.Session()
        self.session.headers = self.headers

    def get_songurls(self, playlist):
        '''进入所选歌单页面，得出歌单里每首歌各自的ID 形式就是“song?id=64006"'''
        url = self.main_url + 'playlist?id=%d' % playlist
        re = self.session.get(url)  # 直接用session进入网页，懒得构造了
        sel = Selector(text=re.text)  # 用scrapy的Selector，懒得用BS4了
        songurls = sel.xpath('//ul[@class="f-hide"]/li/a/@href').extract()
        return songurls  # 所有歌曲组成的list
        ##['/song?id=64006', '/song?id=63959', '/song?id=25642714', '/song?id=63914', '/song?id=4878122', '/song?id=63650']

    def get_songinfo(self, songurl):
        '''根据songid进入每首歌信息的网址，得到歌曲的信息
        return：'64006'，'陈小春-失恋王'''
        url = self.main_url + songurl
        re = self.session.get(url)
        sel = Selector(text=re.text)
        song_id = url.split('=')[1]
        song_name = sel.xpath("//em[@class='f-ff2']/text()").extract_first()
        singer = '&'.join(sel.xpath("//p[@class='des s-fc4']/span/a/text()").extract())
        songname = singer + '-' + song_name
        return str(song_id), songname

    def download_song(self, songurl, dir_path):
        '''根据歌曲url，下载mp3文件'''
        song_id, songname = self.get_songinfo(songurl)  # 根据歌曲url得出ID、歌名
        song_url = 'http://music.163.com/song/media/outer/url?id=%s.mp3' % song_id
        path = dir_path + os.sep + songname + '.mp3'  # 文件路径
        request.urlretrieve(song_url, path)  # 下载文件

    def work(self, playlist):
        songurls = self.get_songurls(playlist)  # 输入歌单编号，得到歌单所有歌曲的url
        dir_path = r'C:\Users\HP\Desktop\Music'
        for songurl in songurls:
            self.download_song(songurl, dir_path)  # 下载歌曲


if __name__ == '__main__':
    d = wangyiyun()
    d.work(2008272804)
    # ```
