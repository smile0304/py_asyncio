def gen_func():
    # try:
    yield "http://www.baidu.com/"
    # except Exception as e:
    #     pass
    yield 2
    yield 3
    return "TT"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception,"Download error")
    print(next(gen))