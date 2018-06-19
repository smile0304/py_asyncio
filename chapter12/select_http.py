#使用select完成http请求
import socket
from urllib.parse import urlparse
from selectors import DefaultSelector,EVENT_READ,EVENT_WRITE

#非阻塞IO实现http请求
#select + 回调 + 事件循环

selector = DefaultSelector()
urls = ["https://www.baidu.com"]
stop = False

def loop():
    # 时间循环，不停的请求socket的状态并调用回调函数
    #1.select本身是不支持register模式，
    #2.socket状态变化后的回调，是程序员完成的
    while not stop:
        ready = selector.select()
        for key,mask in ready:
            call_back = key.data
            call_back(key)
    #回调+时间循环+select(poll/epoll)

class Fether:
    def connted(self,key):
        selector.unregister(key.fd)
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readalab)

    def readalab(self,key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self,url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = '/'
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass
        #注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connted)




if __name__ == "__main__":
    fetcher = Fether()
    fetcher.get_url("https://www.baidu.com")
    loop()