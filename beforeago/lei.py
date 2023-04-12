# 开发时间： 2022/7/30  10:44
# 开发人：林坚洪
class Student:
    native_pace='吉林'#类属性
    def __init__(self, name, age, sg):
        self.name=name
        self.age=age
        self.__sg=sg

    def sk(self):#封装性例子，在类里面调用函数输出
        print(self.__sg)

    #实例方法
    def eat(self):
        print('吃饭了')

    #静态方法
    @staticmethod
    def method():
        print('我是静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('cls，我是类方法')

'''stu1=Student('张三',20)
stu1.eat()
print(stu1.name)
Student.eat(stu1)'''


s1=Student('贾金宝1',11,170)
s2=Student('贾金宝2',65,118)
print()
print(s1.native_pace)
print(s2.native_pace)
Student.native_pace='天下'
print(s1.native_pace)
print(s2.native_pace)
print()
Student.cm()
Student.method()

s1.xb='女'
print(s1.name,s1.age,s1.xb)#动态绑定性别属性
print(s2.name,s2.age)
print()

def show():#类之外称为变量
    print('动态绑定类方法')

s1.show=show()
s1.show
print(s1.name)
print(s1.age)


s1.sk()#封装性
