#python 中垃圾回收机制是采用引用计数
a = object()
b =a
del a
print(b)
print(a)

class A:
    def __del__(self):
        pass