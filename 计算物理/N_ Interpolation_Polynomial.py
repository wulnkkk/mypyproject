#利用牛顿插值法进行函数拟合  注：学习函数递归法
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号

def creatbasefun(x,X,m):  #创建基函数
    ans=1
    if m!=0:
        ans=(x-X[m-1])*creatbasefun(x,X,m-1)
    return ans

def creatDQ(X,Y,m,i=0):     #计算差商
    '''
    m表示差商的阶数
    i标记差商的起点
    '''
    if m==0:
        dq=Y[i][0]
    else :
        dq=(creatDQ(X,Y,m-1,i+1)-creatDQ(X,Y,m-1,i))/(X[i+m][0]-X[i][0])
    return dq

def fun(x,X,Y):     
    num=X.shape
    num=num[0]
    ans=0
    for i in range(num):
        base=creatbasefun(x,X,i)
        dq=creatDQ(X,Y,i)
        ans+=dq*base
    return ans


x=np.array([[2.20],[ 2.40],[ 2.60] ,[2.80], [3.00]])
y=np.array([[0.78846], [0.87547], [0.95551], [1.02962], [1.09861]])
for i in range(5): # 验证差商计算
    for j in range(i+1):
        print("{:.5f}".format(creatDQ(x,y,j,i-j)),end=" ")
    print()

plt.scatter(x,y,8,"r")
plt.plot(np.linspace(2,3,1000),fun(np.linspace(2,3,1000),x,y),'b',label="拟合曲线") 
plt.legend()
