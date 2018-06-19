#python和java的变量不一样
#python的变量实质上是一个指针


a = 1
a = "abc"
#a贴在1上
# 先生成对象，在贴便利贴

a = [1,2,3]
b =a
print(id(a),id(b))
print( a is b)
b.append(4)
print(a)


# a = [1,2,3]
# b = [1,2,3]
#
# print(a == b )
# print(a is b )


class People:
    pass

person = People()
if type(person) is People:
    print("yes")