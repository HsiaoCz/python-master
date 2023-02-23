# 抽象基类
# 有点类似于接口
# python中变量只是一个符号而已
# 抽象基类：在基础类当中设定一个方法
# 所有继承这个类的类需要覆盖这个方法

# 抽象基类的适用场景:
# 我们去检查这个类是否具有某种方法


class Company(object):

    def __init__(self, company_list) -> None:
        self.company_list = company_list

    def __len__(self):
        return len(self.company_list)

com = Company(["helllo", "hii"])
print(hasattr(com, "__len__"))

# isinstance() 可以判断某个类是否是某种类型
# 在某些情况下希望判断某个对象的类型

from collections.abc import Sized

isinstance(com, Sized)

# 我们需要强制某个子类必须实现某些方法
# 实现了一个web框架，集成cache(redis,cache,memorycache)
# 需要设计一个抽象基类，指定子类必须实现某些方法

# 如何去模拟一个抽象基类?


class CacheBase():

    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


class RedisCache(CacheBase):
    pass

# python内置已经实现了一些通用的抽象基类
# 放在collections.abc模块里面
