#coding:utf-8

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

#请用sorted()对上述列表分别按名字排序
def by_name(t):
    return t[0].lower()


L2 = sorted(L, key=by_name)
print(L2)


#再按成绩从高到低排序：
def by_name(t):
    return t[1]


L2 = sorted(L, key=by_name,reverse=True)
print(L2)
