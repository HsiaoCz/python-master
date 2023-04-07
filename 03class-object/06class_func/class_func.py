# 类方法，静态方法，实例方法


class Date:

    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    def __str__(self) -> str:
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)

    @staticmethod  # 静态方法
    # python中的静态方法，前边不需要接收self
    # 静态方法调用和普通函数一样，静态方法需要使用类名来点
    # 静态方法有一个问题，就是类名是硬编码的
    # 静态方法将方法提升到类的名称空间里
    # 静态方法的在不需要返回类的属性的时候，是比较好用的
    def parse_form_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    @classmethod
    # 类方法就不会硬编码
    # 可以随着类名的改变而改变
    # 这里主要使用了一个cls，class的简写
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))


if __name__ == "__main__":
    new_day = Date(2023, 12, 31)
    new_day.tomorrow()
    print(new_day)
