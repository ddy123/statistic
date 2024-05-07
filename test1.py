import numpy as np
data = np.array([[5, 12, 1],
                 [6, 21, 0],
                 [14, 5, 0],
                 [16, 10, 0],
                 [13, 19, 0],
                 [13, 32, 1],
                 [17, 27, 1],
                 [18, 24, 1],
                 [20, 20, 0],
                 [23, 14, 1],
                 [23, 25, 1],
                 [23, 31, 1],
                 [26, 8, 0],
                 [30, 17, 1],
                 [30, 26, 1],
                 [34, 8, 0],
                 [34, 19, 1],
                 [37, 28, 1]])
# 得到特征向量
X_train = data[0:6:2, 0:2]

# 得到类别向量
y_train = data[:, 2]
print(X_train);
print(y_train);