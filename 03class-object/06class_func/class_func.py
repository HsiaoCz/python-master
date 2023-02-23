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
    def parse_form_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))


if __name__ == "__main__":
    new_day = Date(2023, 12, 31)
    new_day.tomorrow()
    print(new_day)
