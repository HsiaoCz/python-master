# python当中super函数
# 使用super可以获取到父类

# super的执行顺序

# super并不是调用父类的构造函数
# 而是调用MRO这个顺序的下一个类的构造函数
class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super(D, self).__init__()


if __name__ == "__main__":
    print(D.__mro__)
    d = D()
