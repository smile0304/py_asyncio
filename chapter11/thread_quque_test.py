#通过queue的方式进行同步
#线程间的通信
import time
import threading
from queue import Queue

def get_detail_html(queue):
    #爬取文章详情页
    while True:
        url = queue.get()
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


def get_detail_url(queue):
    #爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")

#线程间的通信方式 - 共享变量

if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)
    thread1 = threading.Thread(target=get_detail_html,args=(detail_url_queue,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_url,args=(detail_url_queue,))
        html_thread.start()
