# 开发时间：2023-04-14 22:45
# 开发人员：林坚洪
# encodeing "UTF-8"
import re

import jieba

jieba.setLogLevel(jieba.logging.INFO)
from snownlp.seg import seg

# fs = open('bili_small.txt', encoding='utf-8')
# s = fs.read()
import jieba.analyse
jieba.analyse.set_stop_words("stop_words.txt")

text = ''
with open('bili_small.txt', encoding='utf-8') as fileIn:
    for line in fileIn.readlines():
        line = line.strip('\n')  # 去除换行符
        line = re.sub(r'[^\u4e00-\u9fa5]', '', line)
    text += ' '.join(jieba.cut(line))
    # words = normal.filter_stop(words)
    text += ' '
print(text)

import numpy as np
from wordcloud import WordCloud, STOPWORDS
from PIL import Image  # 图像处理库

# 若 PIL 导入报错，使用 pip install --upgrade pillow 更新图像界面库 pillow
image = np.array(Image.open('timg.jpg'))  # 将图片转换为二维矩阵
wc = WordCloud(background_color='white',  # 设置背景颜色
               mask=image,  # 设置背景图片
               max_words=100,  # 设置最大现实的字数
               stopwords=STOPWORDS,  # 设置停用词
               font_path='C:/Windows/fonts/simsun.ttc',  # 设置字体格式，中文
               max_font_size=100,  # 设置字体最大值
               random_state=30,  # 设置随机生成状态，即配色方案
               )
wc.generate(text)
import matplotlib.pyplot as plt

plt.imshow(wc)
plt.axis('off')
plt.show()

#
# from snownlp import SnowNLP, normal
# #
# # kk = SnowNLP(s)
# # print(kk.keywords(40))
# import jieba
# import jieba.analyse
# from snownlp import sentiment
# def handle(self, doc):  # 在 sentiment 中
#     words = seg.seg(doc)  # seg 是 snownlp 的分词方法
#     words = normal.filter_stop(words)  # 过滤停用词
#     return words
#
# sent = sentiment.Sentiment()
# words_list = sentiment.Sentiment.handle(sent, s)
#
#
# text = ' '.join(words_list)
# tags = jieba.analyse.extract_tags(text, topK=20)
# print(tags)
