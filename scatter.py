from matplotlib import pyplot as plt
import numpy as np
'''
颜色方式
1.颜色英文
2.英文简写 r,b,g
3.十六进制 #FFAABB
4.数字序列
5.cmap颜色条
'''

#x=np.array([1,2,3,4,5,6,7,8,9]);
#y=np.array([11,2,7,9,23,42,11,22,66]);

x=np.random.rand(50);
y=np.random.rand(50);

#s 散点的面积，c散点的颜色，marker散点的样式,alpha透明度
s=(20*np.random.rand(50))**2;

'''
colors=np.random.rand(50);
plt.scatter(x,y,s,colors);
'''

colors=np.arange(50);
plt.scatter(x,y,s,colors,cmap='Reds');

#再运用plot则画成折线图
#plt.plot(x,y);
plt.show();