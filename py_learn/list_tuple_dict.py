classmates = ['Michael', 'Bob', 'Tracy']
len(classmates)
classmates[0]
classmates[-1]#'Tracy'

classmates.append('Adam')#追加
classmates.insert(1, 'Jack')#也可以把元素插入到指定的位置，比如索引号为1的位置
#要删除list末尾的元素，用pop()方法：
classmates.pip()#'Adam' popped
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
#某个元素替换成别的元素，可以直接赋值给对应的索引位A置

list里面的元素的数据类型也可以不同，比如：
>>> L = ['Apple', 123, True]
list元素也可以是另一个list，比如：
>>> s = ['python', 'java', ['asp', 'php'], 'scheme']


另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：

>>> classmates = ('Michael', 'Bob', 'Tracy')
现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
只有1个元素的tuple定义时必须加一个逗号,，来消除歧义:
t=(1,)

#dict
要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：

>>> 'Thomas' in d
False
二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：

>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1

要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
>>> d.pop('Bob')

#set
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合：

>>> s = set([1, 2, 3])
>>> s
set([1, 2, 3])
注意，传入的参数[1, 2, 3]是一个list，而显示的set([1, 2, 3])只是告诉你这个set内部有1，2，3这3个元素，显示的[]不表示这是一个list。

重复元素在set中自动被过滤
通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：

>>> s.add(4)
>>> s.remove(4)
set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：

>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
set([2, 3])
>>> s1 | s2
set([1, 2, 3, 4])

#!!!注意不可变对象如str和可变对象如list
对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
>>> a = 'abc'
>>> a.replace('a', 'A')
'Abc'#函数返回值变了
>>> a
'abc'#而'abc'本身没变
#再次赋值，a指向新的函数返回值，并非原str变了
a=a.replace('a','A')
