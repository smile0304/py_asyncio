#类也是对象,type创建类的类
def create_class(name):
    if name =="user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

#type动态创建类
#User = type("User",(),{})

def say(self):
    return "i am user"
    #return self.name

class Baseclass:
    def answer(self):
        return "i am base class"

class Metaclass(type):
    #现在就是元类

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls,*args, **kwargs)

#什么是元类，元类就是创建类的类  对象<-class(对象)<-type
class User(metaclass=Metaclass):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "user"

#python中类实例化的过程，会首先寻找metaclass，通过metaclass创建user类
#type取创建类对象


if __name__ == "__main__":
    # MyClass = create_class("user")
    # my_obg = MyClass()
    # print(type(my_obg))

    #User = type("User", (Baseclass,), {"name":"user","say":say})
    my_obj = User(name="TT")
    #print(my_obj.say())
    print(my_obj)