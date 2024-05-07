import matplotlib.pyplot as plt
import numpy as np
import time
#plt.ion()
x=np.arange(10);
y=x**2;
for i in range(10):
    plt.cla();
    if i%2==0:
        plt.plot(x,x);
    else:
        plt.plot(x,y);
    plt.pause(1);
    
#plt.ioff()
#默认情况下show会阻塞后面的程序
#plt.show();
print(123);
