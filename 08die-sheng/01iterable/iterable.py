# 什么是迭代协议
# 迭代器是什么?迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下表的访问方式不一样，迭代器是不能返回的，迭代器提供了一种惰性访问数据的方式
# []背后的原理是__iter__

from collections import Iterable, Iterator
a = [1, 2]
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
