#利用泰勒插值法进行函数拟合
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号

def creatfunc(x,n=0): # 定义范德蒙德多项式矩阵 ,可以用vander函数实现。
    '''
    n 为指定多项式的阶数，不指定默认为x的长度-1
    '''
    num=x.shape  #获得多项式长度
    num=num[0]
    if n == 0: 
        n=num
    X=np.zeros([num,n])
    for i in range(0,num):
        for j in range(0,n):
            X[i,j]=x[i]**j
    return X

def solvefunc(x,y) :#求解多项式系数
    X=creatfunc(x)
    A=np.linalg.solve(X,y)
    return A
def fun(x,A):    #计算拟合后的结果
   num=A.shape
   num=num[0]
   X=creatfunc(x,num)
   y=X.dot(A)
   return y
x=np.array([[0], [100], [300], [1000] ,[1500], [2000]])
y=np.array([[0.9689], [0.9322] ,[0.8969], [0.8515], [0.7984], [0.7485]])
A=solvefunc(x,y)
plt.scatter(x,y,8,"r")
plt.plot(np.linspace(0,2000,100),fun(np.linspace(0,2000,100),A),'b',label="拟合曲线") 
plt.legend()
