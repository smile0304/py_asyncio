#生成器函数，函数中有yield关键字
def gen_func():
    #惰性求值
    yield 1
    yield 2

def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)

def fib2(index):
    re_list = []
    n,a,b = 0,0,1
    while n<index:
        re_list.append(b)
        a,b = b,a+b
        n += 1
    return re_list


if __name__ == "__main__":
    gen = gen_func()#返回一个生成器对象，python编译字节码的时候就产生了
    for value in gen:
        print(value)
    # re = func()
    # pass