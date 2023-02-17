# python的数据模型对python的影响
class Company(object):

    def __init__(self, employee_list) -> None:
        self.employee = employee_list

    # 我们定义了这个个魔法函数之后，就使得我们的类变成了可迭代的对象了
    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

print(len(Company))

# 数据模型对python起的是增强的作用
