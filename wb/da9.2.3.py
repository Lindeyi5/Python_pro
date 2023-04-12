# 开发时间：2023-02-26 19:55
# 开发人员：林坚洪
# encodeing "UTF-8"
class fun1():
    def __init__(self):
        self.a=100
        self.b=200
    def bus(self):
        print('我是公共汽车')

class fun2(fun1):
    def taxi(self):
        print('我是出租车')

f=fun2()
print(f.b)
print(f.a)
f.bus()
f.taxi()
print()

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def nj(self):
        print(self.name,'年纪是',self.age)

class Student(Person):
    def __init__(self,name,age,score):
        #super().__init__(self)
        # super().__init__(name=self.name,age=self.name)
        super().__init__(name,age)
        self.score=score
    def cj(self):
        print(self.name,'成绩是',self.score)
xm=Student('小明',66,99)
xm.cj()
xm.nj()

