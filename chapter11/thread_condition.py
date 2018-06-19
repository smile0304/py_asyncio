import threading

#条件变量，用于复杂的线程间同步

# class XiaoAi(threading.Thread):
#     def __init__(self,lock):
#         super().__init__(name="小爱")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{}:在".format(self.name))
#         self.lock.release()
#         self.lock.acquire()
#         print("{}:好啊".format(self.name))
#         self.lock.release()
#
# class TianMao(threading.Thread):
#     def __init__(self,lock):
#         super().__init__(name="天猫精灵")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{}:小艾同学".format(self.name))
#         self.lock.release()
#         self.lock.acquire()
#         print("{}:我们老对古诗吧".format(self.name))
#         self.lock.release()

from threading import Condition
class XiaoAi(threading.Thread):
    def __init__(self,cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}:在".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}:好啊".format(self.name))
            self.cond.wait()
            self.cond.notify()

class TianMao(threading.Thread):
    def __init__(self,cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        with self.cond:
            print("{}:小艾同学".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}:我们老对古诗吧".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == "__main__":
    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)
    xiaoai.start()
    tianmao.start()
