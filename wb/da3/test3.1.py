# 开发时间：2023-03-08 10:33
# 开发人员：林坚洪
# encodeing "UTF-8"
# importing the necessary libraries
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
# Creating random dataset
z = 4 * np.tan(np.random.randint(10, size=(500))) + np.random.randint(100, size=(500))
x = 4 * np.cos(z) + np.random.normal(size=500)
y = 4 * np.sin(z) + 4 * np.random.normal(size=500)
# Creating figure
fig = plt.figure(figsize=(12, 8))
ax = plt.axes(projection="3d")
# Add x, and y gridlines for the figure
ax.grid(b=True, color='blue', linestyle='-.', linewidth=0.5, alpha=0.3)
# Creating the color map for the plot
my_cmap = plt.get_cmap('hsv')
# Creating the 3D plot
sctt = ax.scatter3D(x, y, z, alpha=0.8, c=(x + y + z), cmap=my_cmap, marker='^')
plt.title("3D scatter plot in Python")
ax.set_xlabel('X-轴', fontweight='bold')
ax.set_ylabel('Y-轴', fontweight='bold')
ax.set_zlabel('Z-轴', fontweight='bold')
fig.colorbar(sctt, ax=ax, shrink=0.6, aspect=5)
# display the plot
plt.show()
