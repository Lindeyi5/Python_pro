# 开发时间：2023-04-10 11:17
# 开发人员：林坚洪
# encodeing "UTF-8"
import jieba

jieba.setLogLevel(jieba.logging.INFO)
seg_list1 = jieba.cut("我是一名中国的大学生", cut_all=True)
seg_list2 = jieba.cut("我是一名中国的大学生", cut_all=True, HMM=True)
print(u"全模式    : " + "/ ".join(seg_list1))
print(u"全模式-HMM: " + "/ ".join(seg_list2))

seg_list1 = jieba.cut("我是一名中国的大学生", cut_all=False)
seg_list2 = jieba.cut("电视剧微微一笑很倾城很好看：讲了一个累觉不爱的故事",
                      cut_all=False)
seg_list3 = jieba.cut("石墨烯是好材料", cut_all=False)
print(u"默认模式: " + "/ ".join(seg_list1))
print(u"默认模式: " + "/ ".join(seg_list2))
print(u"默认模式: " + "/ ".join(seg_list3))

seg_list = jieba.cut("我去中国杭州的浙江大学参观")
print(", ".join(seg_list))

seg_list = jieba.cut("结婚的和尚未结婚的人")
print(", ".join(seg_list))

import jieba.posseg as pseg

words = pseg.cut("结婚的和尚未结婚的人")
print(words)
for word, flag in words:
    print('%s%s' % (word, flag))

jieba.load_userdict("userdict.txt")
jieba.add_word('累觉不爱的故事')  # 增加词
test_sent = (
    "电视剧微微一笑很倾城很好看：讲了一个累觉不爱的故事\n 看了非常的蓝瘦香菇，不过石墨烯是好材料。"
)
words = jieba.cut(test_sent)
print('/'.join(words))

print('/'.join(jieba.cut('「小黑牛」会被分词')))

jieba.suggest_freq('小黑牛', True)
print('$'.join(jieba.cut('「小黑牛」不会被分词')))

import jieba.analyse

jieba.analyse.set_stop_words("stop_words.txt")

jieba.add_word('人民的名义')  # 增加词典
content = open('news.txt', 'rb').read()  # 以二进制形式读取文件
tags = jieba.analyse.extract_tags(content, topK=5)  # 取 tfidf 权重前 5 的词
# print(content)
print(','.join(tags))

tags = jieba.analyse.extract_tags(content, topK=5, withWeight=True)
print(tags)

listkey = []
listval = []
for word, val in sorted(tags, key=lambda x: x[1], reverse=True):
    listkey.append(word)
    listval.append(val)
    print(word, val)
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
# plt.rcParams['font.sans-serif'] = ['SimMicrosoft YaHeiHei']# 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False
plt.bar(np.arange(5), listval, log=True)
plt.xticks(np.arange(5), listkey, rotation=30)
ax = plt.gca()  # gca='get current axis'
ax.set_ylabel('tfidf')
# ax.set_yticks([0,0.5,20])
plt.title('词频统计')
plt.show()
