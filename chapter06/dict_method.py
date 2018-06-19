a = {"TT1":{"company":"test"},
     "TT2":{"company":"test"}}
print(a)
#a.clear()
print(a)

#copy，返回浅拷贝
# new_dict = a.copy()
# new_dict["TT1"]["company"] = "kzhl"
# print(new_dict)


#深拷贝
import copy
new_dict = copy.deepcopy(a)
new_dict["TT1"]["company"] = "kzhl"
print(new_dict)

#fromkeys
new_list = ["TT1","TT2"]
new_dict = dict.fromkeys(new_list , "KZHL")
print(new_dict)

print(new_dict.get("TT",{}))

# for key,value in new_dict.items():
#     print(key,value)

#default_value = new_dict.setdefault("TT","213")
#pass


new_dict.update({"TT":"432432"})



new_dict.update(TT10="test",TT11="21321")
new_dict.update(["TT12","test"])
print(new_dict)