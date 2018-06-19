import asyncio
import time
from functools import partial
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end")
    return "TT"

def callback(url,future):
    print(url)

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    #get_future = asyncio.ensure_future(get_html('https://www.baidu.com/'))
    tasks = loop.create_task(get_html('https://www.baidu.com/'))
    tasks.add_done_callback(partial(callback,"http://www.baidu.com"))
    loop.run_until_complete(tasks)
    print(tasks.result())
    print(time.time()-start_time)