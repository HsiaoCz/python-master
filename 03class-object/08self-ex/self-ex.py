# python当中的自省机制
# 自省是通过一定的机制查询到对象的内部结构


class Person:
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == "__main__":
    user = Student("Hello")

    # 通过__dict__查询属性
    # 但是对应列表这种就会抛异常

    print(user.__dict__)

    # 可以通过dict来操控对象的属性
    user.__dict__["school_addr"] = "北京"
    print(user.school_addr)

    # dir获取对象当中的所有属性
    print(dir(user))
