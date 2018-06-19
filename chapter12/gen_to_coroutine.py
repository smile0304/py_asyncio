#生成器是可以暂停的函数
import inspect
import socket
def gen_func():
    value = yield 1
    return "TT"
#用同步的方式编写异步的代码，在适当的时候暂停函数
def get_socket_data():
    yield "TT"

def downloader(url):
    client = socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass
    selector.register(self.client.fileno(), EVENT_WRITE, self.connted)
    source = yield from get_socket_data
    data = source.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)

def downloca_html(html):
    html = yield from downloader()

if __name__ == "__main__":
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except Exception as e:
        pass
    print(inspect.getgeneratorstate(gen))