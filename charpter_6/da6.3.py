# 开发时间：2023-04-03 10:46
# 开发人员：林坚洪
# encodeing "UTF-8"
import nltk
import pandas as pd

# train=pd.read_csv('movieReviews.tsv')
train = pd.read_csv("movieReviews.tsv", header=0, delimiter='\t', quoting=3)
'''
movieReviews.tsv 作为训练数据，tsv 文件意味着这是一个 tab 分割的类 csv 文件
delimiter 参数的值设置为\t
header = 0 在这里表示文件包含列名，通过 head 查看列内容
quoting=3 参数表示忽略双引号
'''
# print(train.head().to_string())
# print(train.shape)
# print(train.columns)
# print(train["review"][0])
# print(train.iloc[:, -1])

from bs4 import BeautifulSoup

example1 = BeautifulSoup(train["review"][0], "html.parser")

# print('-' * 3999)
# print(example1)
# print('-' * 3999)
# print(example1.get_text())
import re

letters_only = re.sub("[^a-zA-Z]", " ", example1.get_text())
print(letters_only)
lower_case = letters_only.lower()
print(lower_case)
words = lower_case.split()
print(words)
from nltk.corpus import stopwords

print(stopwords.words('english'))
print('-' * 3999)
stops = set(stopwords.words("english"))
meaningful_words = [w for w in words if not w in stops]
print('&'.join(meaningful_words))


def review_to_words(raw_review):
    # 去 HTML 标签
    review_text = BeautifulSoup(raw_review, 'html.parser').get_text()
    # 去非字母符号
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
    # 分词并小写化
    words = letters_only.lower().split()
    # 去停止词
    stops = set(stopwords.words("english"))
    meaningful_words = [w for w in words if not w in stops]
    return (" ".join(meaningful_words))


clean_view = review_to_words(train['review'][0])
print(clean_view)

num_reviews = train["review"].size
print(num_reviews)
#
clean_train_reviews = []
# '''
# 利用 for 循环，调用 append 方法不停将清洗之后的评论放入。
# 注意：由于是对 25000 个评论进行操作，这里可能会运行很长时间，需要中途打印信息，已
# 达到提示功能。
# '''
for i in range(0, num_reviews):
    if (i + 1) % 1000 == 0:
        print("已处理 %d 条评论" % (i + 1))
    clean_train_reviews.append(review_to_words(train["review"][i]))
print(clean_train_reviews[0])  # 看第一条评论处理结果，与之前对比

# text = ''
# for i, j in enumerate(clean_train_reviews):
#     text += j
#     text += ' '
#     if (i + 1) % 5000 == 0:
#         print("已处理 %d 条评论" % (i + 1))
text = " ".join(clean_train_reviews)

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

wc = WordCloud(background_color="pink",  # 设置背景颜色
               max_words=50,  # 设置显示的最大词数
               stopwords=STOPWORDS,  # 设置停用词
               max_font_size=100,  # 设置字体最大值
               random_state=30  # 设置随机生成状态，即配色方案
               )
wc.generate(text)  # 产生词云图
plt.imshow(wc)  # 显示词云图
plt.axis('off')  # 取消坐标，美化界面
plt.show()

# tokens=nltk.word_tokenize(text)
# fdist1=nltk.FreqDist(tokens)
# listkey=[]
# listval=[]
tokens = nltk.word_tokenize(text)  # 分词
fdist1 = nltk.FreqDist(tokens)  # 统计词频
listkey = []  # 用来保存所有词
listval = []  # 用来保存所有词对应的词频
# 遍历词频列表项，按第 2 列词频倒序显示，取前 20 个主题词
for key, val in sorted(fdist1.items(), key=lambda x: x[1], reverse=True)[:20]:
    listkey.append(key)
    listval.append(val)
    print(key, val)
import numpy as np
plt.bar(np.arange(20), listval, log=True)
plt.xticks(np.arange(20), listkey, rotation=90)
plt.title('Word Freq')
plt.show()
