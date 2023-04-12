# 开发时间：2023-02-22 11:13
# 开发人员：林坚洪
# encodeing "UTF-8"
class car:
    speed=300
    def __init__(self):
        self.price=150
        self.color='black'
print(car.speed)
#print(car.price)
g1=car()
print(g1.price)
print(g1.color)
print(g1.speed,end='\n'*2)

g2=car()
print(g1.speed)
print(g2.speed)
print(id(g1.speed),id(g2.speed))

car.speed=200
print(g1.speed)
print(g2.speed)
print(id(g1.speed),id(g2.speed))

g1.speed=100
print(g1.speed)
print(g2.speed)
print(id(g1.speed),id(g2.speed))


