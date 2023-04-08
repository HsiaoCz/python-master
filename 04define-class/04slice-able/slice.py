# 切片
# 模式[start:end:step]
# 分别表示开始位置，结束位置和步长
# step为负整数表示反向切片

alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(alist[::2])
print(alist[::-1])

# 切片会返回一个新的元素，不会改变原始序列
# 当起始或者结束位置大于切片的长度的时候，会自动帮我们修正成切片的头尾

# 实现一个可切片的对象


class Group:
    # 支持切片操作

    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        pass

    def __getitem__(self):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        if isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


staffs = ["hello", "hi", "bob"]
group = Group("user", "imooc", staffs)
for user in group:
    print(user)
