import pandas as pd ,numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm 
from scipy.optimize import curve_fit
plt.rcParams ['font.sans-serif'] = ['Simhei']

x=[i for i in range(21)]
y_0=[11652.630,6117.335,3577.815,	2389.621,1816.609,1522.838,	1365.184,1263.21,	1195.879,	1131.615,	1084.473,1043.08,	995.5294	,951.4133	,911.6598,	874.8266,	842.5933	,811.1026	,777.2444,	745.8831,	710.44]
delta=[]
for i in x:   #计数相对误差
    if x in range(2):
        delta.append(1/np.sqrt(y_0[i]*1))
    elif x in range(2,6):
        delta.append(1/np.sqrt(y_0[i]*2))
    elif x in range(6,12):
        delta.append(1/np.sqrt(y_0[i]*2.5))
    elif x in range(12,18):
        delta.append(1/np.sqrt(y_0[i]*3))
    else:
        delta.append(1/np.sqrt(y_0[i]*3.5))
y=[np.log10((y_0[i]-49.83)/(y_0[0]-49.83)) for i in x] # 去除本底计数,并取对数得到相对强度


plt.title("β射线对铝板的吸收曲线")
plt.xlabel("铝板厚度(个数)")
plt.ylabel(r"相对强度 $lg\frac{I}{I_0}$")
plt.xticks(range(0,22,2),[r"{:}$d_0$".format(i) for i in range(0,22,2)])
plt.yticks([-4,-3,-2,-1,0],[r"$10^{-4}$",r"$10^{-3}$",r"$10^{-2}$",r"$10^{-1}$",r"$10^{0}$"])
plt.plot(x,y,label="吸收曲线")
plt.scatter(x,y,10,"r",label="数据点")
for i in x:
    plt.text(i,y[i]+0.043,"{:.2f}%".format(delta[i]*100),fontsize=6)

nx=np.array(x[0:3])  #线性拟合
ny=np.array(y[0:3])
def fuc(x,k,b):   
    y=k*x+b
    return y
pfit,info=curve_fit(fuc,nx,ny)
perr = np.sqrt(np.diag(info)) #返回标准差
plt.plot(np.linspace(0,5),fuc(np.linspace(0,5),pfit[0],pfit[1]),"r--",label="线性拟合曲线")

plt.legend()
plt.show()

