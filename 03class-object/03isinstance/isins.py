# isinstance和type的区别
# isinstance内部会去检查继承链
# is 判断的是id是否相同，也就是是否是同一对象
# ==判断的是值是否相等

class A:
    pass


class B(A):
    pass

b = B()

print(isinstance(b, B))
print(isinstance(b, A))
print(type(b) is A)