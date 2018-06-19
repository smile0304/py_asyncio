class User:
    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls)


    def __init__(self,name):
        self.name = name

#new是用来控制对象的生成过程，在对象生成前调用
#init是用来完善对象的
#如果new方法不返回对象则不会调用init
if __name__ == "__main__":
    user = User(name = "123")
