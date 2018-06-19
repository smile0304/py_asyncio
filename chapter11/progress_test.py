#多进程
#耗cpu的操作，用多线程编程，对于io操作来说，用多线程

#1.对于耗费cpu的操作，多进程优于多线程
import time
from concurrent.futures import ThreadPoolExecutor,as_completed
# from concurrent.futures import ProcessPoolExecutor
# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n-1)+fib(n-2)
#
# print(fib(3))
#
# if __name__ == "__main__":
#     with ThreadPoolExecutor(3) as executor:
#         all_task = [executor.submit(fib, (num)) for num in range(25,40)]
#         start_time = time.time()
#         print("main")
#         for future in as_completed(all_task):
#             data = future.result()
#             print("exec result:{}".format(data))
#         print("last time is {}".format(time.time()-start_time))

def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        print("main")
        for future in as_completed(all_task):
            data = future.result()
            print("exec result:{}".format(data))
        print("last time is {}".format(time.time()-start_time))
