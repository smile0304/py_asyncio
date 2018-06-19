#GIL global interpreter lock
#python红一个线程对应c语言中的一个线程
#gil使得一个线程在一个cpu上执行字节码,无法将多个线程映射到多个cpu上

#gil会根据自省的行数以及时间片释放gil，gil遇到io操作会主动释放

# import dis
# def add(a):
#     a = a+1
#     return a
# print(dis.dis(add))
import threading
total = 0
def add():
    global  total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1

thread1 =threading.Thread(target=add)
thread2 =threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)