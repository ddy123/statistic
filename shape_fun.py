import numpy as np
x=np.array([[1,2],[2,3],[3,4]]);
#shape用来返回包含数组维度的元组，是数组的一个属性而非函数，列表无此属性
#tuple是不可变的有序序列
y=x.shape;
print(y);
