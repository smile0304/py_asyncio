def add(a,b):
    a += b
    return a

class Company:
    def __init__(self,name,staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self,staff_name):
        self.staffs.append(staff_name)

    def remove(self,staff_name):
        self.staffs.remove(staff_name)


if __name__ == "__main__":
    # a = 1
    # b = 2
    # c = add(a,b)
    # print(c)
    # print(a,b)
    #
    # a = [1,2]
    # b = [3,4]
    # c = add(a, b)
    # print(c)
    # print(a, b)
    #
    # a = (1, 2)
    # b = (3, 4)
    # c = add(a, b)
    # print(c)
    # print(a, b)

    com1 = Company("TT",["TT1","TT2"])
    com1.add("TT3")
    com1.remove("TT1")
    print(com1.staffs)

    com2 = Company("C_TT",[])
    com2.add("TT")
    print(com2.staffs)

    com3 = Company("C_TT1",[])
    com3.add("ttxx")
    print(com2.staffs)
    print(com3.staffs)
    print(com3.staffs is com2.staffs)

    print(Company.__init__.__defaults__)