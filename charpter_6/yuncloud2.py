# 开发时间：2023-04-19 10:20
# 开发人员：林坚洪
# encodeing "UTF-8"
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

text = open('ironman.txt').read()
print(text)
from PIL import Image  # PIL 图像处理库
import numpy as np

image = np.array(Image.open('timg.jpg'))  # 将图片转换为二维矩阵
wc = WordCloud(background_color="white",  # 设置背景颜色
               mask=image,  # 设置背景图片
               max_words=50,  # 设置显示的最大词数
               stopwords=STOPWORDS,  # 设置停用词
               max_font_size=100,  # 设置字体最大值
               random_state=30  # 设置随机生成状态，即配色方案
               )
wc.generate(text)
plt.imshow(wc, interpolation='bilinear')  # 双线插值，显示图形
plt.axis("off")
plt.show()
