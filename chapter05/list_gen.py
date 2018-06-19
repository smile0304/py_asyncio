#列表生成式子

def handle_item(item):
    return item*item

odd_list = []
for i in range(21):
    if i%2 ==1:
        odd_list.append(i)

odd_list = [handle_item(i) for i in range(21) if i % 2 == 1 ]


print(odd_list)
#生成器表达式
odd_list = (handle_item(i) for i in range(21) if i % 2 == 1 )
#print(odd_list)
for item in odd_list:
    print(item)


#字典推倒式
my_dict = {"bobby1":22,"bobby2":23,"imooc":5}
reverse_dict = {value:key for key,value in my_dict.items()}
print(reverse_dict)

#集合推导式
my_set = {key for key,value in my_dict.items()}
print(type(my_set))
print(my_set)



