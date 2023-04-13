# 什么是变量
# python中的变量和java中的变量本质是一样的
# python的变量实质是一个指针

a = 1
# 先去内存生成一个对象1，然后让a指向1
a=[1,2,3]
b=a
b.append(4)
print(a)