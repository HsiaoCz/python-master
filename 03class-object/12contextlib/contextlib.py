# 进一步简化上下文管理器

import contextlib


class Sample():
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def do_something(self):
        print("doing something")

# 通常定义一个上下文管理器，需要实现两个魔法函数
# contextlib这个包可以将一个函数包装成一个上下文管理器


@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    yield {}
    print("file end")

# yield之前的相当于enter之中要做的事
# yield之后相当于exit之中的要做的事


with file_open("./.git") as f_opend:
    print("file processing")
