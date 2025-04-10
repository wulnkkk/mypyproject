import pandas as pd ,numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm 
from scipy.optimize import curve_fit
plt.rcParams ['font.sans-serif'] = ['Simhei']
data=[Ti,Cr,Fe,Cu,Zn,Ge]
name=["Ti","Cr","Fe","Cu","Zn","Ge"]
for a in range(6):
    plt.yticks([-4,-3,-2,-1,0],[r"$10^{-4}$",r"$10^{-3}$",r"$10^{-2}$",r"$10^{-1}$",r"$10^{0}$"])
    plt.xlabel("铝片个数)")
    plt.ylabel(r"相对强度 $ln\frac{I}{I_0}$")
    x=np.array(range(8))
    y=[np.log(i/data[a][0]) for i in data[a]]
    plt.scatter(x,y,label="{:}散点".format(name[a]))
    x=np.delete(x,4)    #去除偏离点  
    y=np.delete(y,4)
    #线性拟合
    def fuc(x,k,b):   
        y=k*x+b
        return y
    pfit,info=curve_fit(fuc,x,y)
    perr = np.sqrt(np.diag(info)) #返回标准差
    plt.plot(np.linspace(0,7),fuc(np.linspace(0,7),pfit[0],pfit[1]),"r--",label="{:}的拟合曲线".format(name[a]))
    plt.legend()
    print("k={:}±{:}".format(pfit[0],perr[0]))
    print("b={:}±{:}".format(pfit[1],perr[1]))
    plt.show