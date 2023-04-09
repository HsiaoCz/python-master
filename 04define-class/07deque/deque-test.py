# deque双端队列
# deque是为了在两端高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque

d = deque([1, 2, 3])
d.extendleft(['a', 'b', 'c'])

print(d)

deque(['c', 'b', 'a', 1, 2, 3])

d1 = deque(['a', 'b', 'c', 'd', 'e', 'f'])
# 获取双端队列的长度
print(len(d1))
# 类似于list的索引访问，使用方法与列表的索引一样
print(d[-1])
# 反转输出
print(d1.reverse())
print(d.count('a'))  # 输出元素出现的次数
print(d.index('e'))
print(d.index('c', 0, 3))  # 指定查找区间
# 插入元素
d.insert(0, 1)
print(d)
# remove(value)
# 删除指定元素
d.remove('a')
print(d)

# 对deque进行切片会抛出异常

# rotate把右边元素放到坐标，默认为1
d2 = deque([1, 2, 3, 4, 5, 6])
d2.rotate(2)
print(d2)

# 当传入的参数大于0的时候是从右往左放
# 当传入的参数是小于0的时候，是从左往右放

# 有一个需要注意的地方是，初始化deque的时候可以传递给它一个参数maxlen，如果
# 元素超过maxlen的值，那么就会从deque中的一边删除元素，也就是deque始终保持maxlen最大长度的元素
# 超出会自动弹出
# 指定maxlen后使用insrt会抛出异常
# 删除没问题
