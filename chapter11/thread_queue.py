#线程间的通信
import time
import threading
from chapter11 import variables

def get_detail_html(detail_url_list):
    #爬取文章详情页
    detail_url_list = variables.detail_url_list
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")


def get_detail_url(detail_url_list):
    #爬取文章列表页
    detail_url_list = variables.detail_url_list
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")

#线程间的通信方式 - 共享变量

if __name__ == "__main__":
    thread1 = threading.Thread(target=get_detail_html,args=(detail_url_list,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_url,args=(detail_url_list,))
        html_thread.start()
