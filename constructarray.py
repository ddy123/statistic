import numpy as np
a=np.array([1,2,3,4,5]);
b=np.array((1,2,3,4,5));

#迭代对象
d=np.array(range(10));
#生成器
e=np.array([i**2 for i in range(10)]);
print(type(a));
print(e);
f=np.array([i**2 for i in range(10) if i%2==0]);
print(f);
g=np.array([1,2,3,4,'5']);
print(type(g));
#dtype：强制类型转换
h=np.array([1,2,3,4],dtype=float);
print(h);
i=a;
#值赋值
c=np.array(a);
print(id(a));
print(id(c));
print(id(i));
#ndmin:改变维数
j=np.array([1,2,3,4],ndmin=2);
print(j.ndim,j);
k=np.arange(0,20,2);
print(k);
l=np.arange(20,step=3);
print(l);
#切片操作
#[开始索引:结束索引:步长]
#[2],返回与索引对应的单个元素
#[2:]从开索引开始之后所有的项都被提取
#[2:7] 提取两个索引之间的项，不包括停止索引
#切片操作返回的是原数组的一个视图
m=np.array([[0,1,2],[2,3,4],[3,4,5],[4,5,6]]);
#没有修改原数组
m[m>2];
print(m);
#修改了原数组
m[m%2==1] = -1;
print(m);
n=np.array([1,2,3,4,5]);
print(n[::-1]);