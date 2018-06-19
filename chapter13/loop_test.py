#时间循环+回调(驱动生成器)+epoll(io多路复用)
#使用asyncio

import asyncio
import time
from functools import partial
# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)
#     print("end")
#
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     tasks = [get_html('https://www.baidu.com/') for i in range(10)]
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(time.time()-start_time)
#
# #获取携程的返回值
# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)
#     print("end")
#     return "TT"
#
# def callback(url,future):
#     print(url)
#
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     #get_future = asyncio.ensure_future(get_html('https://www.baidu.com/'))
#     tasks = loop.create_task(get_html('https://www.baidu.com/'))
#     tasks.add_done_callback(partial(callback,"http://www.baidu.com"))
#     loop.run_until_complete(tasks)
#     print(tasks.result())
#     print(time.time()-start_time)

#wait 和 gather的区别
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end")

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html('https://www.baidu.com/') for i in range(10)]
    # loop.run_until_complete(asyncio.gather(*tasks))
    # print(time.time()-start_time)

    #gather和wait的区别
    #gather更高的high-level
    group1 = [get_html('https://www.baidu.com/') for i in range(2)]
    group2 = [get_html('https://www.baidu.com/') for i in range(2)]
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    group1.cancel() #取消任务
    loop.run_until_complete(asyncio.gather(*group1, *group2))
    print(time.time()-start_time)