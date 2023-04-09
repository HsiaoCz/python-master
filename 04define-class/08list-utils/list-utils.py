# 列表中常用的三个功能
# 列表推导式，生成器表达式，字典推导式

a = [i for i in range(21) if i % 2 == 1]
print(a)
print(type(a))

# 逻辑复杂的情况


def hadle_item(item):
    return item*item


a1 = [hadle_item(i) for i in range(21) if i % 2 == 1]

# 生成器表达式
a2 = (i for i in range(21) if i % 2 == 1)
print(type(a2))
a1 = list(a2)

# 字典推导式
my_dict = {"hello": 1, "hi": 2}

hello_dict = {value: key for key, value in my_dict.items()}
print(hello_dict)
