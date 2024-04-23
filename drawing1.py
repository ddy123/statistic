from matplotlib import pyplot as plt
import numpy as np
x=np.arange(10);
y=x;
plt.rcParams['font.sans-serif']=["fangsong"];
plt.rcParams['axes.unicode_minus']=False;
plt.xlabel('x轴');
plt.ylabel('y轴');
plt.title('x=y');

#label与legend配合使用，对该条折线进行说明
plt.plot(x,y,label='一哈');
plt.legend(loc='best');

#text函数对折线上的每个点进行标注，必须要使用元组，前两个参数定位，第三个参数为该位置要显示的信息
for x1,y1 in zip(x,y):
    plt.text(x1,y1,y1)
#网格grid axiox='x'可指定轴
plt.grid(True,linestyle='--',color='red',linewidth='0.5');

#设置图片分辨率，大小信息
#plt.figure(figsize=(8,8),dpi=80);
plt.rcParams['figure.figsize']=(8.0,4.0);
plt.rcParams['figure.dpi']=300;

plt.show();
#xticks,gca,图表的样式设置没看，多子图又是什么