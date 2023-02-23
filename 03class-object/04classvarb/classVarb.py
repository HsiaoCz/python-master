# 类变量和实例变量
# self是实例


class A:
    aa = 1  # 这个aa是类变量

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

a = A(2, 3)  # 这里a是A的实例
print(a.x, a.y, a.aa)  # 访问类的实例可以访问类的实例变量和类变量
print(A.aa)  # aa需要类A来访问
print(A.x, A.y)  # 这里会报错 类无法访问类的实例变量，类只能访问类的类变量

A.aa = 11
a.aa = 100
print(a.x, a.y, a.aa) # 这里输出2,3,100
print(A.aa) # 这里输出11

# 当这样写的时候，实际上是两个值
# A.aa修改类类本身的变量
# a.aa实际上是实例新增了一个aa，和类的变量没关系了