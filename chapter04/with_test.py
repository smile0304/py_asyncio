# def exe_try():
#     try:
#         f_read = open("TT.txt")
#         raise KeyError
#         return 1
#     except KeyError as e:
#         print("Key error")
#         return 2
#     else:
#         print("other error")
#         return 3
#     finally:
#         print("finally")
#         return 4
# if __name__ == "__main__":
#     print(exe_try())

#上下文管理器
class Sample():
    def __enter__(self):
        print("enter")
        #获取资源
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #释放资源
        print("exit")

    def do_something(self):
        print("doing somthing")


with Sample() as sample:
    sample.do_something()
# if __name__ == "__main__":
#     pass