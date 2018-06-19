import numbers
class Group:
    #支持前片操作
    def __init__(self,group_name,company_name,staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        #将数据做一个翻转
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item,slice):
            return cls(group_name=self.group_name,company_name=self.company_name,staffs=self.staffs[item])
        elif isinstance(item,numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        #后面
        return iter(self.staffs)

    def __contains__(self, item):
        #if判断
        if item in self.staffs:
            return True
        else:
            return False

group = Group(company_name="TT",group_name="user",staffs=["TT1","TT2","TT2"])
sub_group = group[:2]
print(len(group))
reversed(group)
if "TT5" in group:
    print("yes")
else:
    print("NO")
print(group.staffs)

