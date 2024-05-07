#subplots是直接分割成很多小区域，不管你画不画都存在，并且每个小区域是独立的。
#subplots函数的功能是创建一个figure对象和一组子图
#subplots函数返回两个对象：一个Figure对象和一个Axes对象数组。Figure对象代表整个图像，而Axes对象代表图像中的单个子图。
from matplotlib import pyplot as plt
import numpy as np
x=np.linspace(-10,10,100)
y1=x**2
y2=x**3
c=list(range(-10,10,4))#格外给一个x刻度的列表
b,a=plt.subplots(1,3,sharex=True,sharey=False)
plt.xticks(c)#使用subplots函数时，修改x轴刻度可一并修改
a1=a[0]
a2=a[2]
a1.plot(x, y1,color='r')
a2.plot(x, y2,color='b')

plt.show()