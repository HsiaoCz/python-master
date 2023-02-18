# 鸭子类型
# 只要走起来像鸭子，看起来像鸭子，那就是鸭子


class Cat(object):

    def say(self):
        print("i am a cat")


class Dog(object):

    def say(self):
        print("i am a dog")


class Duck(object):

    def say(self):
        print("i am a duck")

animal = Cat
animal.say()
# 鸭子类型，所有的类实现一种方法，具有相同的方法名
# 那么这些类就可以归为一种类型
# 在一个类中添加某个函数，或者魔法函数
# 就可以使得类变得更通用
# 这里面主要是用到python的鸭子类型

# 使用魔法函数使得python对象类型分组
# 然后就可以使用这些分组中得方法