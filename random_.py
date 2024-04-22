import numpy as np
from matplotlib import pyplot as plt
#np.random.rand(d0,d1,...)
#0-1小数，d表示维度
print(np.random.rand(4,2));
print(np.random.rand(2,2,2));
a=np.random.rand(10000);
plt.hist(a);
#np.random.randint(low,high=none,size=none,dtype='1')
a1=np.random.randint(2,size=5);
print(a1);
a2=np.random.randint(1,5);
print(a2);
a3=np.random.randint(-5,5,size=(2,2));
print(a3);
a4=np.random.randint(-5,5,size=(2,3,4));
print(a4);
