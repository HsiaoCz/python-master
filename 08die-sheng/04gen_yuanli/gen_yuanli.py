# 生成器的原理
# 函数的运行原理

import dis


def foo():
    bar()


def bar():
    pass

# python.exe会用一个pyEval_EvalFramEx(c 函数)去执行foo函数，
# 首先会创建一个栈帧，这个栈帧实际是一个上下文
# python中一切皆对象，栈帧也是对象，字节码对象
# 当foo调用子函数，又会创建一个栈帧
# 所有的栈帧都会放在堆内存当中
# 这就决定了栈帧可以独立于调用者存在


print(dis.dis(foo))


def gen_func():
    yield 1
    name = "bob"
    yield 2
    age = 30
    return "hello"

gen=gen_func()