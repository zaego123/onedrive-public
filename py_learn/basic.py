#!usr/bin/env python3
#coding:utf-8
#加上如上代码，对文件改变权限后，可以直接./filename.py来运行

#IO
print('hello,world')

#print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：
print('The quick brown fox', 'jumps over', 'the lazy dog')
#The quick brown fox jumps over the lazy dog
#print()会依次打印每个字符串，遇到逗号“,”会输出一个空格。
print('100 + 200 =', 100 + 200)

#input()函数
name=input()
name = input('please enter your name: ')
print('hello,', name)

#转义字符\来标识，比如：
print('I\'m \"OK\"!')
#表示的字符串内容是：I'm "OK"!
#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
print(r'///t//')

#and,or,not
#True,False
#//,%
