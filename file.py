import numpy as np
data=np.loadtxt("D:\code\\vs\python\\test.txt",dtype=np.uint32);
print(data,data.shape);

data1=np.loadtxt("D:\code\\vs\python\\test1.txt",dtype=str,encoding='utf-8');
print(data1,data1.shape);

#自定义数据
user_info=np.dtype([('name','U10'),('age','i1'),('height','i2'),('gender','U1')]);
print(user_info);
data2=np.loadtxt("D:\\code\\vs\\python\\test3.txt",dtype=user_info,skiprows=1,encoding='utf-8');
print(data2)
print(data2['age']);
#计算女生的平均身高
isgirl=data2['gender']=='女';
print('女生的身高',isgirl);
print('全体身高:',data2['height']);
print('女生身高',data2['height'][isgirl]);
print('女生平均身高:',data2['height'][isgirl].mean());
#数据中存在空值处理 使用converters参数传递一个字典，key为列索引，value为对列中的值处理
#csv文件默认以逗号为分隔符
#data3=np.loadtxt("D:\\code\\vs\\python\\test2.csv",dtype=user_info,delimiter=',',skiprows=1);
#print(data3);

#skiprows跳过几行，从1开始，usecols选择哪几列，索引从0开始
#converters={列索引:处理的函数,key1:value}
def parse_height(height):
    try:
        return int(height);
    except:
        return 0;
user_info1=np.dtype([('name','U10'),('height','i2')]);
data4=np.loadtxt("D:\\code\\vs\\python\\test2.csv",delimiter=',',skiprows=1,usecols=(1,2),converters={1:parse_height});
print(data4);
