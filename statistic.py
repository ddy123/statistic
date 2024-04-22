import numpy as np
#求平均值mean
m1=np.arange(20).reshape((4,5));
print(m1);
print(m1.mean());
#axis=0从上至下，求每列的平均值
print(m1.mean(axis=0));
#axis=1从左至右，求每行的平均值
print(m1.mean(axis=1));
#求中位数 np.median()
print(np.median(m1[0]));
print(np.median(m1[0,...]));
print(np.median(m1[...,0]));
#平均值 np.std()
print(np.std(m1[0]));
m2=np.arange(10);
m2+=2;
print(m2)
#最大值max(),最小值min()
print(m2.max());
print(m1.max(axis=1));
#加权平均值 np.average(a,axis,weight);
m3=np.array([80,85,90]);
weight=np.array([0.2,0.3,0.5],dtype=float);
av=np.average(m3,weights=weight);
print(av);