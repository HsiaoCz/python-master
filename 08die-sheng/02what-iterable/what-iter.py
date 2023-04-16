# 迭代器和可迭代对象
from collections.abc import Iterable, Iterator

a = [1, 2]
iter_itor = iter(a)
print(isinstance(a, Iterable))
print(isinstance(iter_itor, Iterator))


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __iter__(self):
        return 1


if __name__ == "__main__":
    company = Company(["alex", "hello", "jane"])
    for item in company.employee:
        print(item)
