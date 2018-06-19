def gen_func():
    #1.可以产出值
    #2.可以接受值,
    html = yield "http://www.baidu.com/"
    print("html:", html)
    yield 2
    yield 3
    return "TT"
#throw close

#1.生成器不知可以产生值，也可以接受值

if __name__ == "__main__":
    gen = gen_func()
    url = next(gen)
    print(url)
    #在调用send发送非None之前，必须启动一次生成器，方式有两种next,或者send(None)
    #url = gen.send(None)
    #download url
    html = "TT_ html tst"
    print(gen.send(html)) #send可以传递值放到生成器内部，同时还可以重启生成器执行到下一个yield位置
    #1.启动生成时的方式有两种,next(),send
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))