# 开发时间： 2022/7/30  10:44
# 开发人：林坚洪
'''
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
x=C('杰克',20)
print(x)
print(x.__dict__)
print(C.__dict__)
print(x.__class__)
print(C.__base__)#距离C最近的类
print(C.__bases__)
print(C.__mro__)
print(C.__subclasses__())
print(A.__subclasses__())'''


a=20
b=100
c=a+b
d=a.__add__(b)
print(c,d)
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __add__(self, other):
        return self.name+other.name,self.age+other.age
    def __len__(self):
        return len(self.name)
x1=Student('杰克杰克六税两费',20)
x2=Student('电话',33)
print(x1.__dict__)
x3=x1+x2
print(x3)
print(len(x1))






