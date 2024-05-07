from iotdb.Session import Session
import numpy as np
from matplotlib import pyplot as plt
x=np.arange(10);
plt.plot(x,x);
y=x**2;
# 清除当前图形的内容
plt.cla();
plt.plot(x,y);
plt.show();
