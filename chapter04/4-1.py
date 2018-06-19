class Cat(object):
    def say(self):
        print("I an a cat")

class Dog(object):
    def say(self):
        print("I an a Dog")

class Duck(object):
    def say(self):
        print("I an a Duck")

animal_list = [Cat,Dog,Duck]
for animal in animal_list:
    animal().say()

a= ["TT1","TT2"]
b= ["TT2","TT1"]
name_tuple = ["TT3","TT4"]
name_set = set()
name_set.add("TT5")
name_set.add("TT6")
a.extend(name_tuple)

print(a)