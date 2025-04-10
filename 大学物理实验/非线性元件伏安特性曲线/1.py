import numpy as np
from  matplotlib import pyplot as plt
plt.rcParams ['font.sans-serif'] = ['Simhei']
plt.rcParams['axes.unicode_minus'] = False
import pandas as pd
from scipy.optimize import leastsq  # 导入 scipy 中的最小二乘法工具
df=pd.read_excel(r"data\非线性元件伏安特性曲线\稳压二极管.xlsx")
plt.figure("伏安特性曲线",[8,6],dpi=120)
plt.scatter(df['U(V)'],df['I(mA)'])
plt.xlabel('U(V)')
plt.xticks(np.linspace(-1,-3,15),["{:.1f}".format(i) for i in np.linspace(-1,-3,15) ])
plt.yticks(np.arange(0,20,2),)
plt.ylabel('I(mA)')
plt.title('稳压二极管的伏安特性曲线')
##曲线拟合
def fitfunc4(p, x):  # 定义拟合函数
    p0, p1= p  # 拟合函数的参数
    y = p0*(np.exp(p1*x)-1)  # 拟合函数的表达式
    return y

def error4(p, x, y):  # 定义观测值与拟合函数值的误差函数
    err = fitfunc4(p,x) - y  # 残差
    return err
# 创建给定数据点集 (x,yObs)
x = df['U(V)']
yObs=df['I(mA)']
# 用 scipy.optimize.leastsq() 进行指数函数拟合
p0 = [0.0038, -2]  # 设置拟合函数的参数初值
pFit, info = leastsq(error4, p0, args=(x,yObs))  # 最小二乘法求拟合参数
print(pFit, info)
new_x=np.linspace(-1,-3,500)
yFit = fitfunc4(pFit,new_x )  # 由拟合函数 fitfunc 计算拟合曲线在数据点的函数值
plt.plot(new_x, yFit, '-b', label='伏安特性曲线')
print("Polynomial fitting by scipy.optimize.leastsq")
print("y = p0*(np.exp(p1*x)-1) ")  # 拟合函数的表达式
print("p[0] = {:.4f}\np[1] = {:.4f}".format(pFit[0], pFit[1]))
# 给定点切线
U= -2.737 #由图中给出近似值
I= fitfunc4(pFit,U)#由模型计算出y值
def df(p,x):
    p0, p1= p  # 拟合函数的参数
    y = p0*p1*np.exp(p1*x)  # 拟合函数的表达式
    return y
yk=lambda x : df(pFit,U)*(x-U)+I #切线方程
plt.text(-1.5,15,'切线的横截距k={:.5f}'.format(-I/(df(pFit,U))+U), weight='medium')##切线斜率
plt.plot(np.linspace(-2.386,-3,20),yk(np.linspace(-2.386,-3,20)),'--',label='稳压处切线')
plt.legend()
plt.show()