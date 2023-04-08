# with上下文管理器
# try except finally

try:
    print("code started")
    raise IndexError
except KeyError as e:
    print("key error")

else:
    print("other error")

finally:
    print("finally")

# finally 不管有没有异常，都执行
# 当finally里面有return 的时候，return 这里面的语句

# 上下文管理器协议


class Sample():
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def do_something(self):
        print("doing something")

# 进入的时候执行enter，离开的时候执行exit
# 由python解释器自动执行
# 可以在enter函数内获取资源，exit函数内释放资源