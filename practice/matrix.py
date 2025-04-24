import numpy as np

# 创建一个二维数组作为矩阵
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("矩阵1：")
print(matrix1)
# 创建另一个矩阵
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("矩阵2：")
print(matrix2)

#创建特殊矩阵
# 创建一个 3x3 的全零矩阵
zero_matrix = np.zeros((3, 3))
print("全零矩阵：")
print(zero_matrix)
# 创建一个 3x3 的全一矩阵
ones_matrix = np.ones((3, 3))
print("全一矩阵：")
print(ones_matrix)
# 创建一个 3x3 的单位矩阵
identity_matrix = np.eye(3)
print("单位矩阵：")
print(identity_matrix)

#矩阵的基本运算
# 矩阵加法
result_add = matrix1 + matrix2
print("矩阵加法结果：")
print(result_add)
# 矩阵减法
result_subtract = matrix1 - matrix2
print("矩阵减法结果：")
print(result_subtract)
# 逐元素乘法（Hadamard 乘积）
result_multiply = matrix1 * matrix2
print("逐元素乘法结果：")
print(result_multiply)
# 矩阵乘法（矩阵乘积）
result_dot = np.dot(matrix1, matrix2)
print("矩阵乘法结果：")
print(result_dot)
# 矩阵转置
transpose_matrix1 = matrix1.T
print("矩阵1的转置：")
print(transpose_matrix1)
# 计算矩阵的行列式
det_matrix1 = np.linalg.det(matrix1)
print("矩阵1的行列式：", det_matrix1)
# 计算矩阵的逆
inv_matrix1 = np.linalg.inv(matrix1)
print("矩阵1的逆矩阵：")
print(inv_matrix1)
# 计算矩阵的特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(matrix1)
print("矩阵1的特征值：", eigenvalues)
print("矩阵1的特征向量：")
print(eigenvectors)
# 奇异值分解
U, S, Vt = np.linalg.svd(matrix1)
print("SVD分解结果：")
print("U：")
print(U)
print("S：", S)
print("Vt：")
print(Vt)
# 奇异值分解
U, S, Vt = np.linalg.svd(matrix1)
print("SVD分解结果：")
print("U：")
print(U)
print("S：", S)
print("Vt：")
print(Vt)
# QR 分解
Q, R = np.linalg.qr(matrix1)
print("QR分解结果：")
print("Q：")
print(Q)
print("R：")
print(R)

#矩阵的其他操作
# 获取矩阵的形状
shape_matrix1 = matrix1.shape
print("矩阵1的形状：", shape_matrix1)
# 获取矩阵的维度
ndim_matrix1 = matrix1.ndim
print("矩阵1的维度：", ndim_matrix1)
# 获取矩阵的大小
size_matrix1 = matrix1.size
print("矩阵1的大小：", size_matrix1)
# 矩阵的切片
sub_matrix1 = matrix1[1:, 1:]
print("矩阵1的切片：")
print(sub_matrix1)
# 矩阵的索引
element = matrix1[1, 2]
print("矩阵1的第2行第3列的元素：", element)
