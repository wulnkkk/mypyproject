#雅可比迭代求解线性方程组
import numpy as np
# 更快的高斯迭代是把每个未知元的计算分离开，每次迭代时可以使用本次迭代时先计算的未知元值
def jacobi(A,b):
    n =A.shape
    n=n[1]
    D=np.zeros([n,n]); # 取出系数矩阵的对角元素
    D[range(0,n),range(0,n)]=A[range(0,n),range(0,n)]
    R=A-D           #分解
    x_0=np.zeros([n,1])
    err=1e-5; #收敛条件
    x_old=x_0
    x=circle(x_old,R,D,b)
    while np.linalg.norm(x_old-x)>err:
        x_old=x
        x=circle(x_old,R,D,b)
    X=x
    return X
def circle(x_0,R,D,b): #雅可比跌代的矩阵形式
    x=np.dot(np.linalg.inv(D),(b-np.dot(R,x_0)))
    return x
A=np.array([[10 ,-1, -2,],[-1, 10, -2],[-1, -1 ,5]])
b=np.array([[7.2] ,[8.3] ,[4.2]])
X=jacobi(A,b)