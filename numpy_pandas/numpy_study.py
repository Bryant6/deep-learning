import numpy as np

# ====================================================
# numpy 的基本属性
# ====================================================
array = np.array([[1, 2, 3],
                 [2, 3, 4]])
print(array)
print("number of dim: ", array.ndim)
print("shape: ", array.shape)
print("size: ", array.size)

# ====================================================
# numpy array的创建
# ====================================================
a = np.array([2, 23, 4], dtype=np.float32)
print(a.dtype)

b = np.zeros((3, 4), dtype=int)
print(b)
b = np.ones((3, 4), dtype=int)
print(b)
b = np.empty((3, 4))
print(b)
b = np.arange(10, 20, 2)    # [10 12 14 16 18]
print(b)
b = np.arange(12).reshape((3, 4))
print(b)
b = np.linspace(1, 10, 5)   # [ 1.    3.25  5.5   7.75 10.  ]
print(b)

# ====================================================
# numpy 基本运算
# ====================================================
a = np.array([10, 20, 30, 40])
b = np.arange(4)
print(a, b)
print(a-b, a+b)
print(a**2)     # 平方
print(np.sin(a))
print(b < 3)

A = np.array([[1, 1],
              [0, 1]])
B = np.arange(4).reshape((2, 2))
print(A, '\n', B)
print(A * B)        # 逐个相乘
print(np.dot(A, B))     # 矩阵乘法
print(A.dot(B))

a = np.random.random((2, 4))        # 0-1
print(a)
print(np.sum(a), np.min(a), np.max(a))
print(np.sum(a, axis=1), np.min(a, axis=0), np.max(a, axis=1))      # axis=1(行)

A = np.arange(2, 14).reshape((3, 4))
print(A)
print(np.argmin(A))     # 最小值索引
print(np.mean(A), A.mean(), np.average(A))       # 平均值
print(np.median(A))     # 中位数
print(np.cumsum(A))     # 累加
print(np.diff(A))       # 累差
print(np.nonzero(A))
print(np.sort(A))       # 逐行排序
print(np.transpose(A), A.T)
print(np.clip(A, 5, 9))
print(np.mean(A, axis=0))

# ====================================================
# numpy 索引
# ====================================================
A = np.arange(3, 15)
B = A.reshape((3, 4))
print(A)
print(B)
print(A[3])
print(B[1][1], B[1, 1])
for row in A:
    print(row)

print(A.flat)

# ====================================================
# numpy array 合并
# ====================================================
A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
print(np.vstack((A, B)))        # 向下合并
print(np.hstack((A, B)))        # 向右合并
print(A[np.newaxis, :])
print(A[:, np.newaxis])
print(np.concatenate((A, B, B, A, A), axis=0))

# ====================================================
# numpy array 分割
# ====================================================
A = np.arange(12).reshape((3, 4))
print(A)
print(np.split(A, 3, axis=0))
print(np.array_split(A, 3, axis=1))         # 允许不等分割
print(np.vsplit(A, 3))
print(np.hsplit(A, 2))

# ====================================================
# numpy array copy
# ====================================================
a = np.arange(4)
print(a)
b = a
c = a
d = b
a[0] = 11
print(a, b is a)

b = a.copy()        # 仅赋值
print(b is a)







