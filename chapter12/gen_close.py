def gen_func():
    try:
        yield "http://www.baidu.com/"
    except GeneratorExit:
        raise StopIteration
    yield 2
    yield 3
    return "TT"


if __name__ == "__main__":
    gen = gen_func()
    next(gen)
    gen.close()
    next(gen)