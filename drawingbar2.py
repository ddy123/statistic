from matplotlib import pyplot as plt
import numpy as np
#绘制叠图
plt.rcParams['font.sans-serif']=["fangsong"];
countries=['挪威','德国','中国','美国','瑞典'];
#注意这里要使用数组，因为数组才能相加silver_medal+bronze_medal，列表使用'+'会拼接成一个新列表
gold_medal=np.array([16,12,9,8,8]);
silver_medal=np.array([8,10,4,10,5]);
bronze_medal=np.array([13,5,2,7,5]);
width=0.2;
plt.bar(countries,gold_medal,color='gold',label='金牌',bottom=silver_medal+bronze_medal,width=width);
plt.bar(countries,silver_medal,color='silver',label='银牌',bottom=bronze_medal,width=width);
plt.bar(countries,bronze_medal,color='#A0522D',label='铜牌',width=width);
plt.ylabel('奖牌数');

#设置图例
plt.legend(loc='upper right');
plt.show();