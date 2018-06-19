class Company(object):
    def __init__(self,employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

com = Company(["TT1","TT2","TT3"])

#我们在某些情况下，判定某些对象的类型
#from collections.abc import Sized
from collections.abc import *
#print(hasattr(com,"__len__"))
print(isinstance(com,Sized))
#print(len(com))

#强制某些子类必须实现的某些方法
#实现一个框架，集成cache(redis,memachary,cache)
#需要设计一个抽象积累，指定子类必须实现某些方法

#如何去模拟一个抽象基类

import abc

# class CachBase():
#
#     def get(self,key):
#         raise NotImplementedError
#
#     def set(self,key,value):
#         raise NotImplementedError
#
# class RedisCache(CachBase):
#
#     def set(self,key,value):
#         print("set")
#
# redis_cache = RedisCache()
# redis_cache.set("key","value")
import abc

class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self,key):
        pass

    @abc.abstractmethod
    def set(self,key,value):
        pass


class RedisCache(CacheBase):
    pass
    # def set(self,key,value):
    #     print("set")

redis_cache = RedisCache()
