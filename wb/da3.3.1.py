# 开发时间：2023-03-06 10:02
# 开发人员：林坚洪
# encodeing "UTF-8"
import pandas as pd
#
test = pd.read_csv("csvTest.csv")
# print(test.head())
# print(test.describe().loc[['mean', 'std'], :].round(2))
# for i in range(2):
#     print(test.)

import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
for i in range(2):
    axes[i].scatter(test.iloc[:, i], test.iloc[:, 2])
plt.show()
