#对于io编程来说，多线程性能差别不大
#1.通过thread类实例化
import time
import threading


def get_detail_html(html):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")


# if __name__ == "__main__":
#     thread1 = threading.Thread(target=get_detail_html,args=("",))
#     thread2 = threading.Thread(target=get_detail_url,args=("",))
#     start_time = time.time()
#     #thread2.setDaemon(True)
#     thread1.start()
#     thread2.start()
#     print("las time :{}".format(time.time() - start_time))
#     thread1.join()
#     thread2.join()
#
#     print("las time :{}".format(time.time()-start_time))

#2.通过竭诚threading类
class GetDetailHtml(threading.Thread):
    def __init__(self,name):
        super(GetDetailHtml, self).__init__(name=name)

    
    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

class GetDetailUrl(threading.Thread):
    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")

if __name__ == "__main__":
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl()
    start_time = time.time()
    thread1.start()
    thread2.start()
    thread2.join()
    thread2.join()