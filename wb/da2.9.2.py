# 开发时间：2023-02-26 16:21
# 开发人员：林坚洪
# encodeing "UTF-8"
class Car():
    def run(self):
        print('随风奔跑自由是方向')

    def re_turn(self):
        print('回来吧')

    def re_turn2(self):
        print('不回来吧')


# Car.run()
g1 = Car()
g1.run()
g1.re_turn()

Car().re_turn2()
print('*' * 88)


class man():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def cry(self):
        print('%s正在哭' % self.name)

    def girl(self):
        print('%s都%s岁了还在泪流满面'%(self.name,self.age))


man1 = man('小明', 330, '男')
man1.cry()
man1.girl()
