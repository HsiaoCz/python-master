class Company(object):

    def __init__(self, employee_list) -> None:
        self.employee = employee_list

    # 我们定义了这个个魔法函数之后，就使得我们的类变成了可迭代的对象了
    def __getitem__(self, item):
        return self.employee[item]

company = Company(["tom", "bob", "jane"])

# emploee = company.employee
for i in company:
    print(i)

# 魔法函数 所谓的魔法函数，就是以双下划线开头的，以双下划线结尾的
# 魔法函数并不是和类挂钩的，而是增强类的
# 如果拿不到迭代器，就会去找类里面有没有getitem魔法函数
# 魔法函数既不是继承自基类的，也不是属于类本身的，它只是对类的一种增强