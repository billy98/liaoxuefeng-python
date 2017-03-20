#coding:utf-8

L1 = ['Hello','World',18,'Apple',None,]
L2 = [x.lower() for x in L1 if isinstance(x,str)]

L3 = ['Hello','World',18,'Apple',None,'Baiducom']
L4 = [x.lower() for x in L3 if isinstance(x,str) if len(x) > 5]



print (L2)
print (L4)
