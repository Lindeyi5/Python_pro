# 开发时间：2023-03-06 10:36
# 开发人员：林坚洪
# encodeing "UTF-8"
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 2, 100)
# print(x)
y1 = x ** 3 + 5 * x ** 2 + 10
# # plt.plot(x,y1)
# # plt.show()
#
y2 = 3 * x ** 2 + 10 * x
# # plt.plot(x,y2)
y3 = 6 * x + 10
# plt.plot(x,y3)
# plt.show()

# fig, ax = plt.subplots(figsize=(12, 7))
# ax.plot(x, y1, c='b', label="y(x)")
# ax.plot(x, y2, c='g', label="y'(x)")
# ax.plot(x, y3, c='r', label="y''(x)")
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.legend()
# plt.show()
# fig.savefig('figure-1.pdf')

fig, ax = plt.subplots(figsize=(12, 7))
ax.plot(x, y1, lw=3, c='b', label="$y(x)$")
ax.plot(x, y2, lw=3, c='g', label="$y'(x)$")
ax.plot(x, y3, lw=3, c='r', label="$y''(x)$")
ax.plot(x, np.zeros_like(x), lw=2, color='black')
ax.plot([-3.33, -3.33], [0, (-3.33) ** 3 + 5 * (-3.33) ** 2 + 10], ls='--', lw=1, color='pink')
ax.plot([0, 0], [0, 10], ls='--', lw=1, color='pink')
ax.plot([0], [10], lw=3, marker='o', color='blue')
ax.plot([-3.33], [(-3.33) ** 3 + 5 * (-3.33) ** 2 + 10], marker='o', lw=1, color='blue')
ax.set_ylim(0, 40)
ax.set_yticks([-10, 0, 10, 20, 30])
ax.set_xticks([-4, -2, 0, 2])
ax.set_xlabel("$x$", fontsize=18)
ax.set_ylabel("$y$", fontsize=18)
ax.legend(loc=0, ncol=3, fontsize=14, frameon=False)
plt.show()
