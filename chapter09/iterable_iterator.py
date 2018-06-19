from collections.abc import Iterator
class Company(object):
    def __init__(self,employee_list):
        self.employee = employee_list

    def __iter__(self):
        #变为可迭代对象
        return MyIterator(self.employee)
#迭代器
class MyIterator:
    def __init__(self,employee_list):
        self.iterlist = employee_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        #返回迭代值的逻辑
        try:
            word = self.iterlist[self.index]
        except IndexError:
            raise StopIteration
        self.index+=1
        return word

if __name__ == "__main__":
    company = Company(["tom","bob","jane"])
    my_itor = iter(company)
    # while True:
    #     try:
    #         print(next(my_itor))
    #     except StopIteration:
    #         pass

    #my_itor = iter(company)
    for item in company:
        print(item)