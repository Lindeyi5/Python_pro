# 开发时间： 2022/7/30  20:43
# 开发人：林坚洪
'''class Student():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0},年龄是{1}'.format(self.name,self.age)

stu=Student('张三',22)
print(stu.__str__())'''

#重写父类方法
class Animal():
    def eat(self):
        print('dw')

class Dog(Animal):
    def eat(self):
        print('gou')

class Cat():
    def eat(self):
        print('mao')

class Person():
    def eat(self):
        print('rcw')


def fun(se):
    se.eat()

fun(Dog())
fun(Cat())
fun(Animal())
fun(Person())