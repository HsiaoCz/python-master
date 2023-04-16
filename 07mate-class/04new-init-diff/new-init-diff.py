# __new__和__init__的区别
class User:
    def __new__(cls, *args, **kwargs):
        print("in new")

    def __init__(self, name):
        self.name = name

# new允许在生成对象之前添加逻辑，传递的是类
# __init__传递的是对象，在__new__之后调用
# 两者的本质区别在于，__new__在对象生成之前调用
# __new__用啦控制对象生成过程，在对象生成之前
# __init__是用来完善对象的
# 如果__new__方法不返回对象，则不会调用init函数


if __name__ == "__main__":
    user = User(name="bob")
