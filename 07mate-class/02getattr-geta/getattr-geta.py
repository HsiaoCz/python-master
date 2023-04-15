# __getattr__和__getattribute__
# __getattr__就是在查找不到属性的时候调用
# __getattribute__访问一个不存在的也能访问到
from datetime import date


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __getattr__(self, item):
        print("not find attr")

    def __getattribute__(self, item):
        return "alex"


if __name__ == "__mian__":
    user = User("bob", date(year=1982, month=1, day=1))
    print(user.name)
