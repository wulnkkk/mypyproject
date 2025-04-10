#利用最小二乘法进行线性回归计算
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号
#二元线性回归
def calculatcon(X,Y):#计算系数
    n=X.shape
    n=n[0]
    xbar=np.mean(X)
    ybar=np.mean(Y)
    xsqu=np.sum(X**2)
    b=(np.sum(X*Y)-n*xbar*ybar)/(xsqu-n*xbar**2)
    a=ybar-b*xbar
    return a,b
X=np.array([2,3,5,8,10,12])
Y=np.array([2,4,7,9,10,13])
ans=calculatcon(X,Y)
print(ans)
plt.scatter(X,Y)
plt.plot(X,ans[1]*X+ans[0])
plt.show()

#多元线性回归

# 示例数据
data = np.array([
    [1000, 2, 200000],
    [1500, 3, 300000],
    [1200, 2, 250000],
    [1800, 4, 400000],
    [2000, 3, 450000]
])

# 定义自变量X和因变量y
X = data[:, :-1]  # 自变量
y = data[:, -1]   # 因变量

# 构建设计矩阵X
X = np.hstack((np.ones((X.shape[0], 1)), X))  # 添加全1的列

# 计算回归系数
beta = np.linalg.inv(X.T @ X) @ X.T @ y

# 打印回归系数
print(f"截距项 (β0): {beta[0]}")
print(f"回归系数 (β1, β2): {beta[1:]}")

# 使用模型进行预测
new_data = np.array([
    [1600, 3],
    [1400, 2]
])
new_data = np.hstack((np.ones((new_data.shape[0], 1)), new_data))  # 添加全1的列
predicted_prices = new_data @ beta
print(f"预测价格: {predicted_prices}")

def curvefit(Y,X_list):
    '''
    这里Y的格式为行向量[y1,y2,y3,...],同样对应的X_list应为[X1,X2,X3,...]
    '''
    n=Y.shape 
    n=n[0]
    m=X_list.shape
    m=m[1]
    A=np.ones([n,m+1])  #转化为线性方程形式，但系数是未知数
    A[:,:m]=X_list
    b=np.ones([n,1])
    for i in range(n):
        b[i]=Y[i]
    X=np.dot(np.linalg.inv(np.dot(A.T,A)),np.dot(A.T,b))         #利用最小二乘推出的系数公式
    return  X

def fun(x,A):
    return np.dot(x,A[:-1])+A[-1]
Y=y
X = data[:, :-1]
A=curvefit(Y,X)
print(A)

new_data = np.array([
    [1600, 3],
    [1400, 2]
])
new_data = np.hstack((new_data,np.ones((new_data.shape[0], 1)) ))  # 在最后添加全1的列
predicted_prices = new_data @ A
print(f"预测价格: {predicted_prices}")


