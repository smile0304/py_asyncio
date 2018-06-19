import socket
from urllib.parse import urlparse

def get_url(url):
    #通过socker请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = '/'
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #client.setblocking(False)
    client.connect((host,80))

    #不停的询问链接是否建立好,需要while循环不停的去检查状态
    #做计算任务或者再次发送其他链接请求

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path,host).encode("utf8"))
    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    print(data)
    client.close()

if __name__ == "__main__":
    get_url("http://www.baidu.com/")