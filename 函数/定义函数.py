#coding:utf-8

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x < 0:
        return -x
    else:
        return x

print (my_abs(10))

#以下为作业
    #计算说明：
    #http://baike.baidu.com/link?url=mfUQ5SECC8GsZTEzgdlNLtCoYurrLG8WH6qNqVF3QWcxWSzGJPUtj66KVNOz6Kkp4Vbhq7l7u0cp74wu_HbJ8a

import math

def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('a bad oprtand type')
    if not isinstance(b,(int,float)):
        raise TypeError('b bad oprtand type')
    if not isinstance(c,(int,float)):
        raise TypeError('c bad operand type')

    delta = b**2 - 4*a*c
    if delta >= 0:
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x1,x2
    else:
        print ('此方程无解')

print (quadratic(2,3,1))
print (quadratic(1,3,-4))
print (quadratic(-2,3,4))
