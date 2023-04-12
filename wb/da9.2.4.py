# 开发时间：2023-02-26 20:24
# 开发人员：林坚洪
# encodeing "UTF-8"
from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    def s(self):
        return round(self.r * self.r * pi, 3)

    def d(self):
        return round(self.r * 2 * pi, 3)


c1 = Circle(1)
print(c1.s())
print(c1.d())
print()


class Ring:
    def __init__(self, ri, ro):
        self.ri = Circle(ri)
        self.ro = Circle(ro)

    def area(self):
        return self.ro.s() - self.ri.s()

    def ss(self):
        return self.ro.d() - self.ri.d()

Ring1=Ring(10,20)
print(Ring1.area())
print(Ring1.ss())