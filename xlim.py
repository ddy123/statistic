# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
h = plt.plot(np.arange(0, 10), np.arange(0, 10))
#xlim()函数用于获取或设置当前轴的x限制。
plt.xlim([-5, 200])
plt.title(" matplotlib.pyplot.xlim() Example")
plt.show()
