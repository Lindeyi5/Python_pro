# 开发时间：2023-02-16 10:06
# 开发人员：林坚洪
# encodeing "UTF-8"
print("猜字游戏")
import random
sec=random.randint(1,20)
guess=0
while guess!=sec:
    temp=input("请猜猜数字:")
    guess=int(temp)
    if guess==sec:
        print("你猜对了")
        break
    if guess>sec:
        print("哈哈哈，猜大了哟")
        continue
    if guess<sec:
        print("哈哈哈，猜小了哟")
        continue
print("game over")
