#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
#需要处理的字符串
str = 'a-,a b? c c c c +d+d+d:e:ee: ee aa'
#替换标点为空格，用正则更好
for sp in ',-+?():':
	str = str.replace(sp,' ')
#创建一个列表，存储单词
w_list = str.split(' ')
print w_list
#创建一个空字典
map1= dict()
#去除''
for word in w_list:
    if '' in w_list:
	    w_list.remove('')
print w_list
#遍历字典列表
for word in w_list:
	if(word in map1):
		map1[word]=map1.get(word)+1
	else:
		map1[word]=1

print map1
count_w_list = map1.items()
count_w_list.sort()
#按首字母排序
for str in count_w_list:
    print str