import pandas as pd ,numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm 
from scipy.optimize import curve_fit
from scipy.integrate import quad
plt.rcParams ['font.sans-serif'] = ['Simhei']
df1=pd.read_csv(r"D:\zty\Documents\mypyproject\现代实验\实验三\能谱数据1.csv",header=5,encoding="ANSI")
# plt.scatter(df1.iloc[:,0],df1.iloc[:,1],3,label="散点")
# plt.plot(df1.iloc[:,0],df1.iloc[:,1],"r")
# plt.xlabel("道址道数")
# plt.ylabel("计数数目")
# plt.title("Am的α能谱图")
# plt.show()
# b=[5995.32,
# 5954.86,
# 5642.33,
# 5630.57]
# a=[5485.6,
# 5442.9,
# 5156.59,
# 5144.3
# ]
# def fuc(x,k,b):
#     return k*x+b
# pFit, info = curve_fit(fuc, np.array(a),np.array(b)) 
# perr = np.sqrt(np.diag(info)) #返回标准差
# plt.scatter(a,b,label="散点")
# plt.plot(a,[fuc(x,pFit[0],pFit[1]) for x in a],"r",label="拟合曲线")
# plt.title("能量-道址校准曲线")
# plt.xlabel("能量KeV")
# plt.ylabel("道址数")
# plt.legend()

# def fuc(x,k,b):
#     return k*x+b
# pFit, info = curve_fit(fuc, np.array(range(8)),np.array(a)) 
# perr = np.sqrt(np.diag(info)) #返回标准差
# plt.scatter(range(8),a,label="散点")
# plt.plot(range(8),[fuc(x,pFit[0],pFit[1]) for x in range(8)],"r",label="拟合曲线")
# plt.title("铝箔片数-厚度曲线")
# plt.xlabel("片数")
# plt.ylabel("厚度(μm)")
# plt.legend()

def Sigma_e(E,A_1,A_2,A_3,A_4,A_5):
    a=A_1*E**A_2
    b=A_3/E*1000*np.log(1+A_4/E*1000+A_5*E/1000)
    y=a*b/(a+b)
    return y

def dE(E):
    c=10*10*12*1.4/192*6.026*10*Sigma_e(E,4.232,0.3877, 22.99,35,7.993)
    o=4*4*16*1.4/192*6.026*10*Sigma_e(E,1.776,0.5362,37.11,15.24,2.804)
    h=8*8*1.4/192*6.026*10*Sigma_e(E,0.9661, 0.4126,6.92,8.831,2.582)
    y=(c+o+h)/192
    return 1/y
b=[5485.6,5164.18,4827.91,4475.21,4101.17]
dx=[quad(dE,5485.6,x) for x in b] #b 为穿过不同厚度的能峰