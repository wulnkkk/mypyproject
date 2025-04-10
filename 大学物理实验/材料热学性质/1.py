import numpy as np
import matplotlib.pyplot as plt
plt.rcParams ['font.sans-serif'] = ['Simhei']
import pandas as pd
from scipy.optimize import leastsq  # 导入 scipy 中的最小二乘法工具
#数据处理
data=pd.read_excel(r'D:\mypyproject\data\材料热学性质\铝圆柱体的冷却曲线.xlsx')##数据存放位置
data['T(K)']=data['T（C）']+273.15
##散点图
t=np.linspace(0,15,16)
fig0=plt.figure(0,figsize=[8,6],dpi=90)
plt.scatter(t,data['T(K)'],20,'r')
plt.xticks(np.arange(0,15))
plt.xlabel('t(min)')
plt.ylabel('T(K)')
plt.title('铝圆柱体的冷却曲线')
##曲线拟合
def fitfunc4(p, x):  # 定义拟合函数
    p0, p1, p2, p3 ,p4= p  # 拟合函数的参数
    y = p0 + p1*x + p2*x*x + p3*x*x*x+ p4*x*x*x*x  # 拟合函数的表达式
    return y

def error4(p, x, y):  # 定义观测值与拟合函数值的误差函数
    err = fitfunc4(p,x) - y  # 残差
    return err
# 创建给定数据点集 (x,yObs)
x = t
yObs=data['T(K)']
# 用 scipy.optimize.leastsq() 进行多项式函数拟合
p0 = [1, 1, 1, 1,1]  # 设置拟合函数的参数初值
pFit, info = leastsq(error4, p0, args=(x,yObs))  # 最小二乘法求拟合参数
new_x=np.linspace(0,15,500)
yFit = fitfunc4(pFit,new_x )  # 由拟合函数 fitfunc 计算拟合曲线在数据点的函数值
plt.plot(new_x, yFit, '-b', label='拟合曲线')
print("Polynomial fitting by scipy.optimize.leastsq")
print("y = p[0] + p[1]*x + p[2]*x^2 +p[3]*x^3+p[4]*x*x*x*x")  # 拟合函数的表达式
print("p[0] = {:.4f}\np[1] = {:.4f}\np[2] = {:.4f}\np[3] = {:.4f}".format(pFit[0], pFit[1], pFit[2], pFit[3],pFit[4]))
##给定点切线
T=51.16+273.15
t= 2.961 #由图中给出近似值
def df(p,x):
    p0, p1, p2, p3 ,p4= p  # 拟合函数的参数
    y = p1+ 2*p2*x + p3*x*x*3+ p4*x*x*x*4  # 拟合函数的表达式
    return y
yk=lambda x : df(pFit,t)*(x-t)+T #切线方程
plt.text(11.6,326,'切线斜率k={:.5f}'.format(df(pFit,t)), weight='medium')##切线斜率
plt.plot(np.linspace(0,15,15),yk(np.linspace(0,15,15)),'--',label='平衡温度处切线')
plt.legend()
plt.show()