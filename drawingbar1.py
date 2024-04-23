from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=["fangsong"];
countries=['挪威','德国','中国','美国','瑞典'];
gold_medal=[16,12,9,8,8];
silver_medal=[8,10,4,10,5];
bronze_medal=[13,5,2,7,5];
width=0.2;
#将x轴转换为数值
x=np.arange(len(countries));
#金牌起始位置
gold_x=x;
#银牌起始位置
silver_x=x+width;
#铜牌起始位置
bronze_x=x+2*width;
plt.bar(gold_x,gold_medal,width=width,color='gold');
plt.bar(silver_x,silver_medal,width=width,color='silver');
plt.bar(bronze_x,bronze_medal,width=width,color='saddlebrown');
# plt.bar(countries,gold_medal,color='gold',width=width);
# plt.bar(countries,silver_medal,color='silver',width=width);

plt.xlabel('国家');
plt.ylabel('奖牌数');

#将x标签位置居中，并将其坐标变回来。第一个参数改变x标签的位置，第二个参数将x标签进行映射。va和ha改变字位置
plt.xticks(x+width,labels=countries);
for x1,y1 in zip(gold_x,gold_medal):
    plt.text(x1,y1,y1,va='bottom',ha='center');
for x2,y2 in zip(silver_x,silver_medal):
    plt.text(x2,y2,y2,va='bottom',ha='center');
# for x3,y3 in zip(bronze_x,bronze_medal):
#     plt.text(x3,y3,y3);
for i in range(len(countries)):
    plt.text(bronze_x[i],bronze_medal[i],bronze_medal[i],va='bottom',ha='center');



plt.show();