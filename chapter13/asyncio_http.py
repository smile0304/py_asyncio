#asynic 没有提供http协议的接口 aiohttp
import asyncio
import socket
from urllib.parse import urlparse

async def get_url(url):
    #通过socker请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = '/'

    reader, writer = await asyncio.open_connection(host,80)
    writer.write(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    #不停的询问链接是否建立好,需要while循环不停的去检查状态
    #做计算任务或者再次发送其他链接请求
    all_lines=[]
    async for raw_line in reader:
        data = raw_line.decode("utf8")
        all_lines.append(data)
    html = "\n".join(all_lines)
    print(html)
    return html

async def main(loop):
    tasks = []
    for url in range(20):
        url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx={}&tn=baidu&wd=1&rsv_pq=fccf599e00001493&rsv_t=3337XVJsmCzMIW9h2jR66kjQbmXryuDnGEjZEHGx1OL97CVZUuebjcResQE&rqlang=cn&rsv_enter=0&rsv_sug3=2&rsv_sug1=2&rsv_sug7=101&inputT=1186&rsv_sug4=1848".format(
            url)
        tasks.append(asyncio.ensure_future(get_url(url)))
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)


if __name__ == "__main__":
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()

    loop.run_until_complete(main(loop))
    print(time.time()-start_time)