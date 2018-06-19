class A():
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B,C):
    def __init__(self):
        print("D")
        super().__init__()

#
# from threading import Thread
# class Mythread(Thread):
#     def __init__(self,name,user):
#         self.user = user
#         super().__init__(name=name)

if __name__ == "__main__":
    d =D()
    print(D.__mro__)
