# 类也是对象，type创建类的类

def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

# 灵活的创建动态类
# 使用type,type可以创建类
# User=type("User",(),{})

# 什么是元类，元类是创建类的类
# type就是元类


class MateClass(type):
    pass

# python中的实例化过程，会首先寻找mateclass,通过mateclass去创建user类
# type去创建类对象，实例


class Hello(mateclass=MateClass):
    pass


def say(self):
    return "i am user"


class BaseClass:
    def answer(self):
        print("i am answer")


if __name__ == "__main__":
    Myclass = create_class("user")
    my_obj = Myclass()
    print(my_obj)

    User = type("User", (BaseClass,), {"name": "user", "say": say})
    my_obj = User()
    print(my_obj.name)
