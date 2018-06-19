# __getattr__ ,__getattribute__
#__getattr__  查找不到属性的时候调用
from datetime import date,datetime
class User:
    def __init__(self,info={}):
        self.info = info


    def __getattr__(self, item):
        #print(item)
        #return "not find attr"
        return self.info[item]

    # def __getattribute__(self, item):
    #     return "TT123"


if __name__ == "__main__":
    user = User(info={"company_name":"baidu","name":"TT"})
    print(user.name)
