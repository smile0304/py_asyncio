#使用多线程:在协程中集成阻塞IO
import asyncio
import socket
from concurrent.futures import ThreadPoolExecutor
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
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    tasks =[]
    for url in range(20):
        url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx={}&tn=baidu&wd=1&rsv_pq=fccf599e00001493&rsv_t=3337XVJsmCzMIW9h2jR66kjQbmXryuDnGEjZEHGx1OL97CVZUuebjcResQE&rqlang=cn&rsv_enter=0&rsv_sug3=2&rsv_sug1=2&rsv_sug7=101&inputT=1186&rsv_sug4=1848".format(url)
        task = loop.run_in_executor(executor,get_url,url)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
