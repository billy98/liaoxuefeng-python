#!/usr/bin/env python3
#coding:utf8
# @Date    : 2017-03-20 17:45:33
# @Author  : Billy  5884625@qq.com
# @Link    : http://billy98.blog.51cto.com
# @Version : 1.0

for ch in 'ABC':
    print (ch.lower())


# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：


for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
