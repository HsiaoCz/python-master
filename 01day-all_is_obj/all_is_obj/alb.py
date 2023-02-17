# python中一切都是对象

# python中函数和类也是对象，属于python的一等公民

# 1.赋值给一个变量
# 2.可以添加到集合对象中
# 3.可以作为参数传递给函数
# 4.可以当作函数的返回值

# 将函数赋值给一个变量


def ask(name="bob"):
    print(name)

myfunc = ask
myfunc("zhangsan")


class Person:

    def __init__(self) -> None:
        print("bob")

my_class = Person
my_class()

# 将函数和类添加到集合对象中
obj_list = []
obj_list.append(ask)
obj_list.append(Person)

for i in obj_list:
    print(i)
