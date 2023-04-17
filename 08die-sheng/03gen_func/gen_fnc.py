# 什么是生成器函数
# 只要函数里面有yield,yield返回值给调用方
# yield可以一直返回
def gen_func():
    yield 1
    yield 2
    yield 3

# 惰性求值，延迟求值


def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1)+fib(index-2)


def fib2(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a+b
        n += 1
    return re_list

# 使用生成器实现fb


def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a+b
        n += 1


if __name__ == "__main__":
    # 生成器对象，产生的是一个生成器对象，python编译字节码的时候就产生了
    gen = gen_func()
