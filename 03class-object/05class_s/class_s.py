# 类属性和实例属性以及查找顺序
# 属性：定义在类内部的


class A:
    name = "A"

    def __init__(self) -> None:
        self.name = "hello"  # 这个name属于实例对象


# 当调用a.name会先在实例对象内查找name,如果查找不到才回去类的内部查找
a = A()
print(a.name)


class D:
    pass


class C(D):
    pass


class B(D):
    pass


class A(B, D):
    pass

print(A.__mro__)
