# python中的数据封装和私有属性

class User:
    def __init__(self, birthday):
        self.__brithday = birthday

    def get_age(self):
        # 返回年龄
        return 2023-self.brithday.year


# 如果想要将brithday来隐藏掉
# 在python中使用private
# 这里使用__brithday,这样设置，就无法通过类的实例来访问
# 但是还是可以访问
# 使用user._User__birthday
# 只是一个变形，并不是特别的安全

if __name__ == "__main__":
    user = User(1990-2-1)
    print(user.brithday)
