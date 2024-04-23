from matplotlib import pyplot as plt
import numpy as np
x=np.arange(-50,50);
#上述值作用到x轴，y轴为x值对应的平方
y=x**2;
#数组可以这样对其中的每个元素取平方，列表[1,2,3]则不行

 
#设置图表的名称 plt.title()
#plt.title("y=x^2")
#默认情况不支持中文，修改字体配置
plt.rcParams['font.sans-serif']=["fangsong"];
plt.title("y等于x的平方",fontsize=40);
#修改轴中的负号编码
plt.rcParams['axes.unicode_minus']=False;

#x轴和y轴名称,fontsize设置字体大小 这里字体设置newtimes roman的话不会正常显示中文
plt.xlabel("x轴",fontdict={'family' : 'fangsong', 'size':'20'});
plt.ylabel("y轴");

#好像没用，应该是写错了
plt.rcParams['font.size']=20;

#plot绘制线性图,linewidth调整线条粗细，linestyle调整线条样式，'-'实线, '--'虚线,':'点线,'-.'点划线
plt.plot(x,y,linewidth=4,linestyle='-.');

#绘制第二个图像
y2=x;

#  图例legend(),需要用label打上标签,loc设置标签位置信息upper left,upper center,upper right,center left,
#  center,center right,lower left,lower center,lower right,best
plt.plot(x,y2,label='二哈');
plt.legend(loc='lower left');



plt.show();

#xticks定制坐标轴

#zip将两个列表压缩成一个元组
xlist=[1,2,3,4,5,6];
ylist=[11,12,13,14,15,16];
xy=zip(xlist,ylist);
for x1,y1 in xy:
    print(x1,y1);