# set集合 fronzeset（不可变集合)无序，不重复集合

s = set('abcde')
# s=set(['a'])

m = {"a", "b"}
print(type(m))

print(m)

ss = frozenset("abcde")  # 可以作为dict的key
# print(ss)
# 这个set是不可变的，可以作为dict的key

# 向set添加数据
anthor_set = set('def')
res = s.difference(anthor_set)
print(res)

# 集合运算
