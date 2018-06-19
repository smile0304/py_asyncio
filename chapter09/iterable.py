#什么是迭代协议
#迭代器是什么？ 迭代器是访问集合类元素的一种方式，一般用来遍历数据
#for 迭代器和以下表的访问方式不一样，迭代器不能返回。提供了一种惰性访问数据的方式
#[] __getitem__ , __iter__

from collections.abc import Iterable,Iterator
#Iterable 可迭代对象
#Iterator 迭代器对象

