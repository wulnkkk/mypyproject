import numpy as np
import matplotlib.pyplot as plt
plt.rcParams ['font.sans-serif'] = ['Simhei']
import pandas as pd
import statsmodels.api as sm
from scipy.stats import pearsonr
from scipy.optimize import leastsq 
#数据处理
data=pd.read_excel(r"D:\mypyproject\data\材料热学性质\样品长度随温度变化.xlsx")
##散点图
fig0=plt.figure(0,figsize=[10,6],dpi=90)
plt.scatter(data['t'],data['x'],20,'r')
plt.ylabel('x(mm)')
plt.xlabel('T(℃)')
plt.title('样品长度随温度变化')
r=pearsonr(data['t'],data['x'])[0]#线性相关系数
print(r)
x=sm.add_constant(data['t'])
model=sm.OLS(data['x'],x)
results=model.fit()
new_x=np.linspace(36,79,15)
new_x=sm.add_constant(new_x)
y=results.predict(new_x)
plt.plot(new_x[:,1],y,'r',alpha=1,label='拟合直线')
print(results.summary())
print("Parameters: ", results.params)#斜率及截距
print("Standard errors: ", results.bse)#相应标准误差
plt.xticks(np.arange(35,80,5))
plt.text(33.25,0.329,'斜率k={:.6f}\n标准误差s_k={:.6f}'.format(results.params['t'],results.bse['t']))
##曲线拟合
def fitfunc4(p, x):  # 定义拟合函数
    p0, p1, p2= p  # 拟合函数的参数
    y = p0 + p1*x + p2*x*x  # 拟合函数的表达式
    return y

def error4(p, x, y):  # 定义观测值与拟合函数值的误差函数
    err = fitfunc4(p,x) - y  # 残差
    return err
# 创建给定数据点集 (x,yObs)
x = data['t']
yObs=data['x']
# 用 scipy.optimize.leastsq() 进行多项式函数拟合
p0 = [1, 1, 1]  # 设置拟合函数的参数初值
pFit, info = leastsq(error4, p0, args=(x,yObs))  # 最小二乘法求拟合参数
new_x=np.linspace(35,80,100)
yFit = fitfunc4(pFit,new_x )  # 由拟合函数 fitfunc 计算拟合曲线在数据点的函数值
plt.plot(new_x, yFit, '--b', label='2次拟合曲线')
plt.legend()
plt.show()