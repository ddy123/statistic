import numpy as np
#reshape 改变后的数组元素个数必须与原数组相等
#resize 改变后的数组元素个数可以与原数组不相等，即可任意改变
#np.resize(arr,shape)有返回值，返回复制内容，如果维度不够，会使用原数组数据补齐
#ndarray.resize(shape,refcheck=False)修改原数组，不会返回数据，如果维度不够，会用0补齐
a=np.array([[1,2,3],[4,5,6]]);
print('a数组形状',a.shape);
b=np.resize(a,(3,3));
print(b);
print(a);
a.resize((3,3));
print(a);
#记得append

#返回数组中满足条件的元素
x=np.arange(6).reshape(2,3);
print('我是原数组：',x);
print('我是满足条件的数组：',x[x>2])
#np.argwhere()返回满足条件的索引
y=np.argwhere(x>2);
print(y,y.shape);

#去重 np.unique(arr),该函数还能返回去重后剩余元素的索引
#ui indices=np.unique(a,return_inverse=True)
#返回出现的次数
#ui indices=np.unique(a,return_counts=True)
#np.max(arr) 取最大值
#np.argmax(arr) 取最大值索引
a1=np.array([1,2,3,5,5,6,7,8,2,3]);
print(np.unique(a1));

#排序 np.sort(a) axios=0按列排，axios=1按行排，还可以按字段进行排序
a2=np.array([[6,4,5],[3,6,4]])
b=np.sort(a2,axis=0);
print('排序后的数据为：',b);