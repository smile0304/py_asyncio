# import os
# import time
# pid = os.fork()
# print("TT")
# if pid==0:
#     print('子进程{} , 父进程{}'.format(os.getpid(),os.getppid()))
# else:
#     print("我是父进程:{}".format(pid))
# time.sleep(2)
import multiprocessing

#多进程编程
import time
def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n

# class Myprogress(multiprocessing):
#     def run(self):
#         pass

if __name__ == "__main__":
    # progress = multiprocessing.Process(target=get_html,args=(2,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")

    #使用进程池
    pool = multiprocessing.Pool(3)
    # result = pool.apply_async(get_html,args=(3,))
    # pool.close()
    # pool.join()
    # print(result.get())

    #imap
    # for result in pool.imap(get_html,[1,5,3]):
    #     print("{} sleep success".format(result))

    for result in pool.imap_unordered(get_html,[1,5,3]):
        print("{} sleep success".format(result))
