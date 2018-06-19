#python3.3中添加的新特性

from itertools import chain
my_list = [1,2,3]
my_dict = {
    "TT":"http://blog.smilehacker.net",
    "TT2":"http://www.smilehacker.net"
}

# def g1(iterable):
#     yield iterable
#
# def g2(iterable):
#     yield from iterable
#
# for value in g1(range(10)):
#     print(value)
#
# for value in g2(range(10)):
#     print(value)



def my_chain(*args,**kwargs):
    #print(args)
    for my_iterable in args:
        #yield from iterable
        yield from my_iterable
        # for value in my_iterable:
        #     yield value

for value in my_chain(my_list,my_dict,range(5,10)):
    print(value)

# def g1(gen):
#     yield from gen
#
# def main():
#     g = g1()
#     g.send(None)
#     #1.main 调用方g1(委托生成器) ，gen子生成器
#     #1.yield from 会在调用方与子生成器之间建立一个双向通道 main直接通信gen