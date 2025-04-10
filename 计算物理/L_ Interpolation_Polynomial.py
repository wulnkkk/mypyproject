#利用拉格朗日插值法进行函数拟合
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号

def creatbasefun(x,X,i): #创建拉格朗日基函数
    ans=1
    for p in X:
        if X[i]!=p:
            ans=ans*(x-p)/(X[i][0]-p)
    return ans

def fun(x,X,Y):
    P=0
    num=X.shape
    num=num[0]
    for i in range(num):
        L_i=creatbasefun(x,X,i)
        P=P+Y[i]*L_i
    return P

x=np.array([[0], [100], [300], [1000] ,[1500], [2000]])
y=np.array([[0.9689], [0.9322] ,[0.8969], [0.8515], [0.7984], [0.7485]])
plt.scatter(x,y,8,"r")
plt.plot(np.linspace(0,2000,100),fun(np.linspace(0,2000,100),x,y),'b',label="拟合曲线") 
plt.legend()