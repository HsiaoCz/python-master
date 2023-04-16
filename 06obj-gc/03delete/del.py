# python中垃圾回收的算法采用引用计数

a = 1
b = 0
# 当对象的引用计数为0的时候，python会对对象进行垃圾回收
# del删除对象，只会删除变量和并且使得对象上的引用计数-1
# 并不会直接对对象进行垃圾回收


class A:
    def __del__(Self):
        pass

# 我们可以在对象中定义__del__魔法函数，当python解释器来回收对象的时候，会执行这里面的逻辑