from matplotlib import pyplot as plt
x=range(5);
y=[5,10,15,20,25];
plt.title('基本柱状图');
plt.grid(ls='--',alpha=0.5);
#plt.bar(x,y,facecolor='green');
#color是个列表，可以设置多个颜色
#plt.bar(x,y,color=['r','g','b']);

#设置边缘线条样式edgecolor：ec,linestyle:ls,linewidth:lw
plt.bar(x,y,ec='r',ls='--',lw=2);
plt.show();