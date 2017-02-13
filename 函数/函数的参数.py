#coding:utf-8

#   a b：位置参数 POSITIONAL_OR_KEYWORD
#   c=0：默认参数
#   *args：可变参数  VAR_POSITIONAL
#   **kw：关键字参数  VAR_KEYWORD
#   *后面的为：命名关键字参数   KEYWORD_ONLY

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2,c=3)
f1(1,2,3,'a','b')
#f1(1,2,c=3,'a','b')
#此项会报错SyntaxError: positional argument follows keyword argument
#把c=3赋给了**kw，