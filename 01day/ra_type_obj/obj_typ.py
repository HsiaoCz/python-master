# type、object和class的关系

a = 1
print(type(1))

# 这里会输出class int
print(type(int))

# 这里会输出class type
# a 是int类的实例
# int是type类的对象

print(type(type))
# type 是type类


class Student:
    pass

stu = Student()
print(type(stu))
print(type(Student))
# type -->class--->Student
# 类是由type类生成的一个对象
# object类是所有类默认继承的基类
# object是最顶层的基类

print(type.__bases__())
print(object.__bases__())

# type的基类是object
# object的基类是空，它没有基类
# type(object) --->type
# type(type)---->
# type 既是一个类，也是一个对象
# object是type的一个实例
# type是type的一个对象,type继承object
# 别的类都是type类的实例，但是继承自object
# 而具体的值，如"abc",123是str,int类的实例

# python中的内置类型
# 对象的三个特征：身份、类型、值 所谓的身份就是对象在内存中的地址
# None(全局只有一个)
ms=None
sm=None
print(id(ms)==id(sm))
# None全局只有一个，意思是它的内存地址 

# 数值 int float complex true
# 迭代类型 
# 序列类型 list range tuple str array bytes
# 映射类型dict 字典
# 集合 set
# 上下文管理类型（with)
# 其他类型 模块 class和实例 函数类型 方法类型 代码类型
# object对象 type类型
# ellipisis类型
# notimplement类型