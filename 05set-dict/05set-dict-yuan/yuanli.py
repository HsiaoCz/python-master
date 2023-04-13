# dict查找的性能远大于list
# 在list中随着数据的增大，查找时间会增大
# 在dict中查找元素，不会随着dict的增大而增大
# dict本质是hash表，先将key做hash再与数组偏移量做与运算，确定值存储的位置

# hash一般会存在冲突，python的字典怎么解决hash冲突和扩容的问题？
