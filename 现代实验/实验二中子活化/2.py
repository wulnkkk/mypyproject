import pandas as pd ,numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm 
from scipy.optimize import curve_fit
plt.rcParams ['font.sans-serif'] = ['Simhei']
df1=pd.read_excel(r"D:\zty\Documents\mypyproject\现代实验\实验二\朱天宇202211010110\base11.xlsx",header=1)
df2=pd.read_excel(r"D:\zty\Documents\mypyproject\现代实验\实验二\朱天宇202211010110\source2.xlsx",header=1)
df3=pd.read_excel(r"D:\zty\Documents\mypyproject\现代实验\实验二\朱天宇202211010110\base22.xlsx",header=1)
anum1=dict()
anum2=dict()
anum3=dict()
for i in df1["计数"]:
    if i not in anum1.keys():
        anum1[i]=1
    else:
        anum1[i]+=1
print(anum1)
for i in df2["计数"]:
    if i not in anum2.keys():
        anum2[i]=1
    else:
        anum2[i]+=1
print(anum2)
for i in df3["计数"]:
    if i not in anum3.keys():
        anum3[i]=1
    else:
        anum3[i]+=1
print(anum3)

plt.title("活性净计数衰变曲线")
plt.scatter(df2["ID"],df2["new计数"])
plt.ylabel("计数率（个每秒）")
plt.xlabel("计数时间 （秒）")

def fun( x,p0, p1, p2, p3  ):  # 定义拟合函数
    y = p0*np.exp(-p1*x) + p2*np.exp(-p3*x)   # 拟合函数的表达式
    return y
#使用curve_fit拟合 第一个参数为各个待定参量的拟合值，后一个为协方差矩阵，可从中计算各个参量的方差
pFit, info = curve_fit(fun, np.array(df2["ID"]),np.array(df2["new计数"])) 
perr = np.sqrt(np.diag(info)) #返回标准差