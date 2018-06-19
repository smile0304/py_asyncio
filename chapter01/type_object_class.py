a=1
b="abc"
print(type(1))
print(type(int))
#type->int->1

print(type(b))
print(type(str))
#type->str->abc


class Student:
    pass
print(type(Student))

a=[1,2]
print(type(a))
print(type(list))
print(Student.__bases__)

class My_Student(Student):
    pass
print(My_Student.__bases__)
print(type(object))
print(type(int.__bases__))
print(type(tuple.__bases__))