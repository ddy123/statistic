from matplotlib import pyplot as plt
import numpy as np
x=np.arange(-50,50);
#上述值作用到x轴，y轴为x值对应的平方
y=x**2;
#数组可以这样对其中的每个元素取平方，列表[1,2,3]则不行
plt.plot(x,y)
 