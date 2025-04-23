import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号

dl=np.array([0.998,0.996,0.995,1,1.001,1.001,0.996,0.998])  #mm
d=np.mean(dl)*1e-3   #m
rho=7.8e3  #kg/m**3
rho0=0.95e3  #kg/m**3
D=2e-2    #m
g=9.8    #m/s**2

def fun1(v):
    eta=(rho-rho0)*g*d**2/18/v
    return  eta
def fun2(v):
    eta1=(rho-rho0)*g*d**2/18/v/(1+2.4*d/D)
    return eta1
def fun3(T,A,B):
    return A*np.exp(B/(T+273.15))
# s
t=[[43.22,39.22,37.41,40.13,38.72],[30.75,28.68,28.47,29.57,27.79],[19.81,19.06,19.13,19.32,19.02],[16,15.65,16.13,15.85,16.07],[11.54,14.47,11.65,11.82,11.42]]
s=0.2 #m
tbar=np.mean(t,1)
v=s/tbar
eta=fun1(v)
eta1=fun2(v)
for i in v:
    print('{:.3e}'.format(i))
for i in eta:
    print('{:.3f}'.format(i))
for i in eta1:
    print('{:.3f}'.format(i))


# 拟合与作图
T0=[10,20,30,40]
eta0=[2.42,0.986,0.451,0.231]
T=[25,30,35,40,45] #.C
T_=np.linspace(25,45,100)
# 使用 curve_fit 进行拟合
params0, covariance0 = curve_fit(fun3,T0,eta0, p0=[1, 1000])
params, covariance = curve_fit(fun3,T,eta, p0=[1, 1000])
params1, covariance1 = curve_fit(fun3,T,eta1, p0=[1, 1000])
# 提取拟合参数
A0,B0=params0
A, B= params
A1, B1 = params1
# 打印拟合参数
print(f"拟合参数：A0 = {A0:e}, B0 = {B0:.4f}")
print(f"拟合参数：A = {A:e}, B = {B:.4f}")
print(f"拟合参数：A1 = {A1:e}, B1 = {B1:.4f}")
# 绘制数据点和拟合曲线
plt.figure(dpi=200)
plt.title("蓖麻油的粘滞系数$\eta$随温度T的变化")
plt.xlabel("温度T(℃)")
plt.ylabel("粘滞系数$\eta(Pa\cdot s)$")
plt.scatter(T0[2:],eta0[2:],10,"r",label="标准值数据")
plt.plot(T_,fun3(T_,A0,B0),'r--',label="标准值曲线")
plt.scatter(T,eta,10,label="$\eta$数据")
plt.plot(T_,fun3(T_,A,B),label='$\eta$拟合曲线')
plt.scatter(T,eta1,10,label="$\eta_1$数据")
plt.plot(T_,fun3(T_,A1,B1),label='$\eta_1$拟合曲线')
plt.legend()