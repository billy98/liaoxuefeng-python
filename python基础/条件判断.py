#!/usr/bin/env python3
#coding:utf8
# @Date    : 2017-03-16 15:20:47
# @Author  : Billy  5884625@qq.com
# @Link    : http://billy98.blog.51cto.com
# @Version : 1.0

#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
#用if-elif判断并打印结果：



height = 1.75
weight = 80.5

bmi = weight/(height**2)
print (bmi)

if bmi < 18.5:
    print ("过轻")
elif 18.5 <= bmi <25:
    print ('正常')
elif 25 <= bmi <28:
    print('过重')
elif 28 <= bmi < 32:
    print('肥胖')
else:
    print ('严重肥胖')

