from concurrent.futures import ThreadPoolExecutor,as_completed,wait
from concurrent.futures import Future

#未来对象 Futrue，task的返回容器

#线程池
import time
def get_html(times):
    time.sleep(times)
    print("get page {}".format(times))
    return times


excutor = ThreadPoolExecutor(max_workers=1)
#submit是立即返回
# task1 = excutor.submit(get_html,(3))
# task2 = excutor.submit(get_html,(2))

#要获取已经成功的task的返回
urls = [3,2,4]
all_task = [excutor.submit(get_html,(url)) for url in urls]
#wait(all_task)
#print("main")
for future in as_completed(all_task):
    data = future.result()
    print("get {} page success".format(data))

#通过excutor获取已经完成的task
# for data in excutor.map(get_html,urls):
#     print("get {} page".format(data))
# #done方法用于判定某个人物是否完成
# print(task1.done())
# print(task2.cancel())
# time.sleep(3)
# print(task1.done())
#
# #result 可以获取task的执行结果
# print(task1.result())

