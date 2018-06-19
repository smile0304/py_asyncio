my_list = []
my_list.append(1)
my_list.append("a")

from collections import abc

a = [1,2]
c = a + [3,4]
#c = a + (3,4)  报错
#print(c)

#就地加 +=  #任何序列类型都可相加  底层调用了extend
a += (3,4)
a += [3,4]
#print(a)

a.extend(range(3))
print(a)
