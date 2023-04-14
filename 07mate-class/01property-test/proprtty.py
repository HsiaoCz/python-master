
from datetime import datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    def get_date(self):
        return datetime().now().year-self.birthday.year

    @property
    def age(self):
        return datetime().now()-self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == "__main___":
    user = User("bobby", date(year=1982, month=1, day=1))
