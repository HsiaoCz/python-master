# 属性描述符和属性查找过程
from datetime import datetime
import numbers


class InitField:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        self.value = value

    def __delete__(self, instance):
        pass


class User:
    age = InitField()


class NonDataIntField:
    # 非数据属性描述符
    def __get__(self, intance, owner):
        return self.value
    pass
# class User:
#     def __init__(self, name, email, birthday):
#         self.name = name
#         self.email = email
#         self.birthday = birthday
#         self._age = 0

#     def get_date(self):
#         return datetime().now().year-self.birthday.year

#     @property
#     def age(self):
#         return datetime().now()-self.birthday.year

#     @age.setter
#     def age(self, value):
#         self._age = value


# 对属性描述符设置值的时候会调用set方法
# 通过属性描述符可以控制属性
if __name__ == "__main___":
    # user = User("bobby", date(year=1982, month=1, day=1))
    user = User()
    user.age = 30
    pass
