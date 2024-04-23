from matplotlib import pyplot as plt
import numpy as np

#设置中午字体
plt.rcParams['font.sans-serif']=['SimHei'];
#中文负号
plt.rcParams['axes.unicode_minus']=False;
#设置分辨率
plt.rcParams['figure.dpi']=100;
#设置大小
plt.rcParams['figure.figsize']=(5,3);

#水平条形图
countries=['挪威','德国','中国','美国','瑞典'];
gold_medal=np.array([16,12,9,8,8]);
plt.barh(countries,width=gold_medal);
plt.show();
