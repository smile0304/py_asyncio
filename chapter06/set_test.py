#set 集合
#fronzenset 不可变集合
# 无序，不重复
s = set("abcdee")
print(s)
s = set(["a","b","c","d","e"])
s = {'a','b','c'}
s.add('s')
print(type(s))
print(s)


# s = frozenset('abc')
# print(s)
another_set = set("def")
s.update(another_set)
print(s)
re_set = s.difference(another_set)
print(re_set)