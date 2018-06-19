from datetime import date,datetime
#属性描述符
import numbers
class IntField(object):
    #数据描述符
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise ValueError(" int value need")

        if value < 0:
            raise ValueError("postice value need")
        self.value = value
    def __delete__(self, instance):
        pass

class NonDataIntField:
    #非数据属性描述符
    def __get__(self, instance, owner):
        return self.value

class User:
    age = IntField()
    age = NonDataIntField()

if __name__ == "__main__":
    user = User()
    user.__dict__["age"] = "abc"
    print(user.__dict__)
    #print(user.age)
    #print(getattr(user,'age'))

    # user = User("TT",date(year=1987,month=1,day=1))
    # user.age = 30
    # print(user._age)
    # print(user.age)
