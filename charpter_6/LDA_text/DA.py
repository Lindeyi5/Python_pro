# 开发时间：2023-04-19 10:35
# 开发人员：林坚洪
# encodeing "UTF-8"
import pandas as pd

x = pd.read_csv('doubanpd.csv', encoding="gbk")
print(x.head(10))
newpage = x.dropna(axis=0)
print(newpage.head(10))
import jieba
import jieba.analyse
jieba.setLogLevel(jieba.logging.INFO)
num_reviews = newpage["reviews"].size
print(num_reviews)

textreview = ''
for i in newpage["id"]:
    textreview += newpage["reviews"][i]
    textreview += ' '
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

wc = WordCloud(background_color='white',  # 设置背景颜色
               max_words=50,  # 设置最大现实的字数
               stopwords=STOPWORDS,  # 设置停用词
               font_path='C:/Windows/fonts/simsun.ttc',  # 设置字体格式，中文
               max_font_size=50,  # 设置字体最大值
               random_state=30,  # 设置随机生成状态，即配色方案
               )
wc.generate(textreview)
# 利用 matplotlib 库绘制词云
import matplotlib.pyplot as plt

plt.imshow(wc)
plt.axis('off')
plt.show()

tags = jieba.analyse.extract_tags(textreview, topK=20, withWeight=True)
print(tags)

listkey = []
listval = []
for word, val in sorted(tags, key=lambda x: x[1], reverse=True):
    listkey.append(word)
    listval.append(val)
    print(word, val)
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.bar(np.arange(20), listval, log=True)
plt.xticks(np.arange(20), listkey, rotation=90)
ax = plt.gca()  # gca='get current axis'
ax.set_ylabel('tfidf')
plt.title('词频统计')
plt.show()

documents = newpage['reviews'].values.tolist()
# print(documents)
from nltk.tokenize import word_tokenize

texts_tokenized = []
for document in documents:
    texts_tokenized_unit = []
    for word in word_tokenize(document):
        texts_tokenized_unit += jieba.analyse.extract_tags(word, 5)
    texts_tokenized.append(texts_tokenized_unit)
print(texts_tokenized)

#使用前需要导入 gensim 库，适合本环境的是 2.3 版本，命令：pip install genism==2.3 --no-deps
import gensim
#从 gensim 导入语料库
from gensim import corpora
#建立语料库中词的字典，每个唯一的词作为索引
dictionary = corpora.Dictionary(texts_tokenized)
#将语料库转换成文档词矩阵
doc_term_matrix = [dictionary.doc2bow(doc) for doc in texts_tokenized]
Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(doc_term_matrix, num_topics=6, id2word = dictionary, passes=50)
print(ldamodel.print_topics(num_topics=3, num_words=10))
