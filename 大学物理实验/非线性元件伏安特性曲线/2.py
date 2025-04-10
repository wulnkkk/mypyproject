import numpy as np
from  matplotlib import pyplot as plt
plt.rcParams ['font.sans-serif'] = ['Simhei']
import pandas as pd
from scipy.optimize import leastsq  # 导入 scipy 中的最小二乘法工具
from scipy import optimize as op  
df=pd.read_excel(r"data\非线性元件伏安特性曲线\发光二极管.xlsx")
plt.figure("伏安特性曲线",[8,6],dpi=120)
plt.scatter(df['U1'],df['I1'],color='r')
plt.scatter(df['U2'],df['I2'],color='b')
plt.scatter(df['U3'],df['I3'],color='y')
plt.xlabel('U(V)')
plt.xticks(np.linspace(1.5,3.15,20),["{:.1f}".format(i) for i in np.linspace(1.5,3.15,20) ])
plt.yticks(np.arange(0,30,3),)
plt.ylabel('I(mA)')
plt.title('发光二极管的伏安特性曲线')
#曲线拟合
def fitfunc41(p, x):  # 定义拟合函数
    p0, p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12= p  # 拟合函数的参数
    y = p0+p1*x+p2*x**2+p3*x**3+p4*x**4+p5*x**5+p6*x**6+p7*x**7+p8*x**8+p9*x**9+p10*x**10+p11*x**11+p12*x**12  # 拟合函数的表达式
    return y
def error41(p, x, y):  # 定义观测值与拟合函数值的误差函数
    err = fitfunc41(p,x) - y  # 残差
    return err

def fitfunc4( x,p0,p1):  # 定义拟合函数
    y = p0*(np.exp(p1*x)-1)  # 拟合函数的表达式
    return y

def error4(p, x, y):  # 定义观测值与拟合函数值的误差函数
    err = fitfunc4(p,x) - y  # 残差
    return err

# 创建给定数据点集 (x,yObs)
x = df['U1']
yObs=df['I1']
# 用 scipy.optimize.leastsq() 进行指数函数拟合
p0 = [1,1,1,1,1,1,1,1,1,1,1,1,1]  # 设置拟合函数的参数初值
pFit, info = leastsq(error41, p0, args=(x,yObs),ftol=1e-9,
                    xtol=1e-9,
                    maxfev=100000,
                    epsfcn=1e-10,
                    factor=0.1)  # 最小二乘法求拟合参数
print(pFit, info)
new_x=np.linspace(1.5,3.2,500)
yFit = fitfunc41(pFit,new_x )  # 由拟合函数 fitfunc 计算拟合曲线在数据点的函数值
plt.plot(new_x, yFit, '-r', label='R-led伏安特性曲线')


# 创建给定数据点集 (x,yObs)
x2 = df['U2'][0:16]
yObs2=df['I2'][0:16]
print(x2,yObs2)
# 用 scipy.optimize.leastsq() 进行指数函数拟合
p0 = [1, 1]  # 设置拟合函数的参数初值
pFit2,info= op.curve_fit(fitfunc4, x2,yObs2, p0 =[1, 1])  # 最小二乘法求拟合参
new_x2=np.linspace(2.4,3.3,500)
yFit2=fitfunc4(new_x2,pFit2[0],pFit2[1])
print(pFit2)
plt.plot(new_x2, yFit2, '-b', label='B-led伏安特性曲线')


# 创建给定数据点集 (x,yObs)
x3 = df['U3'][:14]#数据要去除空值
yObs3=df['I3'][0:14]
print(x3,yObs3)
# 用 scipy.optimize.leastsq() 进行指数函数拟合
pFit3, info3 =op.curve_fit(fitfunc4, x3,yObs3, p0 =[1, 1])
print(pFit3, info3)
new_x3=np.linspace(1.5,2.3,500)
yFit3 = fitfunc4(new_x3,pFit3[0],pFit3[1] )  # 由拟合函数 fitfunc 计算拟合曲线在数据点的函数值
plt.plot(new_x3, yFit3, '-y', label='Y-led伏安特性曲线')
# 给定点切线1
U= 2.287 #由图中给出近似值
I= fitfunc41(pFit,U)#由模型计算出y值
def df(x,p):
    p0, p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12= p  # 拟合函数的参数
    y = p1+2*p2*x+p3*3*x**2+4*p4*x**3+5*p5*x**4+6*p6*x**5+7*p7*x**6+8*p8*x**7+9*p9*x**8+10*p10*x**9+11*p11*x**10+12*p12*x**11  # 拟合函数的表达式
      # 拟合函数的表达式
    return y
yk=lambda x : df(U,pFit)*(x-U)+I #切线方程
plt.text(1.5,17,'r切线的横截距k={:.5f}'.format(-I/(df(U,pFit))+U), weight='medium')##切线斜率
plt.plot(np.linspace(1.8,2.2,20),yk(np.linspace(1.8,2.2,20)),'r--',label='r的切线')


# 给定点切线2
U= 3.135 #由图中给出近似值
I= fitfunc4(U,pFit2[0],pFit2[1])#由模型计算出y值
def df(x,p0,p1):
    y = p0*p1*np.exp(p1*x)  # 拟合函数的表达式
    return y
yk=lambda x : df(U,pFit2[0],pFit2[1])*(x-U)+I #切线方程
plt.text(1.5,15,'b切线的横截距k={:.5f}'.format(-I/(df(U,pFit2[0],pFit2[1]))+U), weight='medium')##切线斜率
plt.plot(np.linspace(2.96,3.25,20),yk(np.linspace(2.96,3.25,20)),'b--',label='b的切线')

# 给定点切线3
U= 2.222 #由图中给出近似值
I= fitfunc4(U,pFit3[0],pFit3[1])#由模型计算出y值
def df(x,p0,p1):
    y = p0*p1*np.exp(p1*x)  # 拟合函数的表达式
    return y
yk=lambda x : df(U,pFit3[0],pFit3[1])*(x-U)+I #切线方程
plt.text(1.5,13,'y切线的横截距k={:.5f}'.format(-I/(df(U,pFit3[0],pFit3[1]))+U), weight='medium')##切线斜率
plt.plot(np.linspace(2.08,2.3,20),yk(np.linspace(2.08,2.3,20)),'y--',label='y的切线')


plt.legend()
plt.show()


