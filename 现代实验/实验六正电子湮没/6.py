import pandas as pd ,numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm 
from scipy.optimize import curve_fit
from scipy.signal import find_peaks ,peak_widths
plt.rcParams ['font.sans-serif'] = ['Simhei']

# df0=pd.read_csv(r"D:\zty\Documents\mypyproject\现代实验\实验六正电子湮没\正电子湮没数据30ns-11.csv",encoding="ANSI",header=6)

# plt.title("选择start与stop能窗时的能谱")
# plt.xlabel("道址")
# plt.ylabel("计数")
# plt.plot(df0["Start通道道址"],df0["Start通道计数"])

# df=pd.read_csv(r"D:\zty\Documents\mypyproject\现代实验\实验六正电子湮没\正电子湮没数据30ns-11.csv",encoding="ANSI",header=6)
# plt.title("(0.511MeV,0.511MeV)的寿命谱")
# plt.xlabel("道址")
# plt.ylabel("计数")
# plt.plot(df["Life通道道址"][2300:2600],df["Life通道计数"][2300:2600])
# plt.show()

df=pd.read_csv(r"D:\zty\Documents\mypyproject\现代实验\实验六正电子湮没\正电子湮没数据60ns-21.csv",encoding="ANSI",header=6)
plt.title("延迟为60ns时(1.28MeV,0.511MeV)的寿命谱")
plt.xlabel("道址")
plt.ylabel("计数")
plt.plot(df["Life通道道址"][4800:5100],df["Life通道计数"][4800:5100])
plt.show()
##寻峰与半峰宽
x=find_peaks(df["Life通道计数"][4800:5100],distance=300)
peak_widths(df["Life通道计数"][4800:5100],x)


#曲线拟合
plt.title("延迟为30ns时(1.28MeV,0.511MeV)的寿命谱")
plt.xlabel("时间t_1(ns)")
plt.ylabel("计数")
x=(df["Life通道道址"][2480:3000]-2458)*30/(4927-2472.76) #注意数据的选取，要满足指数近似成立的范围，峰位后几个数据不取。
plt.plot(x,df["Life通道计数"][2480:3000],label="实际数据")
def fuc(x,a1,a2,t1,t2):   
    y=a1*np.exp(-x/t1)+a2*np.exp(-x/t2)
    return y
pfit,info=curve_fit(fuc,x,df["Life通道计数"][2480:3000])
perr = np.sqrt(np.diag(info))    #返回标准差
plt.plot(x,fuc(x,pfit[0],pfit[1],pfit[2],pfit[3]),"r--",label="拟合曲线")
plt.legend()
for i in range(len(pfit)):
    print("c{:}={:.2f}±{:.2f}".format(i,pfit[i],perr[i]))
