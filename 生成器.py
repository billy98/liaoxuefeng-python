#coding:utf-8

'''
杨辉三角定义如下
          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5

'''


def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]


g = triangles()
for n in range(10):
    print(next(g))