from matplotlib import pyplot as plt
import numpy as np
#subplot是一个区域一个区域的画图，逐渐分割
x=np.linspace(-10,10,100)
# 用linspace函数可以生成浮点数列表，但list(range(~))只能强制转换成整数列表
y1=x**2
y2=x**3
#有图像绘制可以不用这句
#plt.figure()
plt.subplot(1,2,1) # 在1行2列的第一列作图，下同理，主打一个分别处理，一个一个写
plt.plot(x,y1)
plt.subplot(1,2,2)
plt.plot(x,y2)
plt.show()
 