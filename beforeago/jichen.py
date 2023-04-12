# 开发时间： 2022/7/30  18:12
# 开发人：林坚洪
# 开发时间： 2022/7/30  10:44
# 开发人：林坚洪
class Person(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def m(self):
        print(self.name,self.age,end='\t')


class Student(Person):
    def __init__(self, name, age,xh):
        super().__init__(name, age)
        self.xh = xh
    def m(self):
        super().m()
        print(self.xh)
       # print(self.name, self.xh)

s1=Student('张三',13,10098)
s1.m()

