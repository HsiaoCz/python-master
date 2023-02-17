# python中的魔法函数
# 1.非数学运算
# 字符串的魔法函数
# 2.数学运算

# 这里定义一个company


class Company(object):

    def __init__(self, employee_list) -> None:
        self.employee_list = employee_list

    def __str__(self) -> str:
        return ",".join(self.employee_list)

    def __repr__(self) -> str:
        return ",".join(self.employee_list)
commpany = Company(["tom", "bob", "jane"])
print(commpany)

# 如果想要输出的company以我们希望的字符串格式
# 可以加上__str__,对对象进行格式化
# 开发模式下使用的__repr__
# 模板函数不用调用，python解释器会自己决定什么时候调用这些函数
# def __abs__(self):
#   return abs(self)  这个魔法函数主要是做数学运算的
# len()这个方法会隐含的调用类的__len__方法
# 像list dict set都是在解释器cpython里面
# 是由c语言写的解释器，性能比较好
# 调用len()函数会直接去cpyhon里读取数据
# 在解释器里面维护了一个值，用来记录set,list,dict的长度
# len()函数会直接读取这个值
# for 遍历类，如果类里有__iter__魔法函数，就会先走这个
# 如果没有，就会走__getitem__这个魔法函数