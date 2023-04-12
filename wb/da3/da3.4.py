# 开发时间：2023-03-06 11:24
# 开发人员：林坚洪
# encodeing "UTF-8"
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 25)
y1 = x ** 3 + 3 * x ** 2 + 10
y2 = -1.5 * x ** 3 + 10 * x ** 2 - 15
# fig, ax = plt.subplots(figsize=(4, 3))
# fig, ax = plt.subplots(1,4,figsize=(12, 2))
fig, ax = plt.subplots(2, 2, figsize=(8, 4))
# ax.plot(x,y1,color='red')
# ax.plot(x,y2)

# ax.step(x,y1)
# ax.step(x,y2)

# ax.bar(x,y1,color='red',width=0.2)
# ax.bar(x,y2,color='blue',width=0.2)

# ax.fill_between(x, y1, y2)

y3 = 4 * x + 5
y4 = 3 * x ** 2 + 2 * x + 2

# ax[0].plot(x,y1)
# ax[1].plot(x,y2)
# ax[2].plot(x,y3)
# ax[3].plot(x,y4)


# ax[0,0].plot(x,y1)
# ax[0,1].plot(x,y2)
# ax[1,0].plot(x,y3)
# ax[1,1].plot(x,y4)

plt.subplot(2, 1, 1)
plt.plot(x, y1)

plt.subplot(2, 2, 3)
plt.plot(x, y2)

plt.subplot(2, 2, 4)
plt.plot(x, y3)

plt.show()
