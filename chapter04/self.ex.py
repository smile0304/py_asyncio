#自省是通过一定的机制查询到对象的内部结构
from chapter04.class_method import Date
class Persion:
    name = "user"

class Student(Persion):
    def __init__(self,school_name):
        self.school_name = school_name

if __name__ == "__main__":
    user = Student("软件学院")

    #通过__dict__查询数据
    #print(Persion.__dict__)
    user.__dict__["school_addr"]="北京"
    print(user.school_addr)
    #print(user.__dict__)
    #print(user.name)
    a=[1,2]
    print(dir(a))