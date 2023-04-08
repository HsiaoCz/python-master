# 序列的三种操作
# + += 和append的区别

a = [1, 2, 3]
c = a+[3, 4]

print(c)
print(id(a))
print(id(c))

# 就地加
a += [3, 4]
print(a)

# +=还可以连接任意的序列类型

a += (23, 14)
print(a)
print(id(a))

# + 只能连接相同的序列，不能为不同的序列
# 可变序列的抽象基类MutableSequence里面有个魔法函数__iadd___
# 当调用+=的时候，就会默认调用这个方法
# 这个魔法函数里有个extend方法
# 会将传递进来的元素进行迭代，并且追加到序列里
# 只要是可迭代的类型都可以

a.append(12)
m = [24, 25]
a.extend(m)

# extend可以迭代追加
# append不会进行迭代
