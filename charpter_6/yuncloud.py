# 开发时间：2023-04-19 9:59
# 开发人员：林坚洪
# encodeing "UTF-8"
import re

import jieba

jieba.setLogLevel(jieba.logging.INFO)

text = open('news.txt').read()
text = ''
with open('news.txt') as fileIn:
    for line in fileIn.readlines():
        line = line.strip('\n')  # 去除换行符
        line = re.sub(r'[^\u4e00-\u9fa5]', '', line)
    text += ' '.join(jieba.cut(line))
    text += ' '
print(text)
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from PIL import Image  # 图像处理库

# 若 PIL 导入报错，使用 pip install --upgrade pillow 更新图像界面库 pillow
image = np.array(Image.open('timg.jpg'))  # 将图片转换为二维矩阵
wc = WordCloud(background_color='white',  # 设置背景颜色
               mask=image,  # 设置背景图片
               max_words=50,  # 设置最大现实的字数
               stopwords=STOPWORDS,  # 设置停用词
               font_path='C:/Windows/fonts/simsun.ttc',  # 设置字体格式，中文
               max_font_size=50,  # 设置字体最大值
               random_state=30,  # 设置随机生成状态，即配色方案
               )
wc.generate(text)
import matplotlib.pyplot as plt

plt.imshow(wc)
plt.axis('off')
plt.show()
