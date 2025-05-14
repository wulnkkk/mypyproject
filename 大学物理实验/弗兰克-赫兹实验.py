import numpy as np                
import matplotlib.pyplot as plt  
import pandas as pd
from scipy.signal import find_peaks
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号
V1=[8,16.6,23,28.6,34.4,40.4,46.2,52.6,58.2,65.4,70.8,78.8]
I1=[0,0.814,0.101,1.317,0.044,1.697,0.134,1.992,0.505,2.304,1.17,2.736]
V2=[8,17,23.2,28.8,34.2,40.6,46,53,58,65.8,70.8,79]
I2=[0,1.448,0.2,2.926,0.093,4.201,0.39,5.371,1.567,6.728,3.761,8.678]
V3=[8,17.8,22.8,28.4,34.4,40.4,46.6,52.4,58.4,65.2,70.9,78.6]
I3=[0,0.049,0.012,0.129,0.011,0.224,0.029,0.314,0.08,0.403,0.203,0.513]
V4=[8,17.2,23,28.8,34.6,40.6,46.4,53,58.4,65.8,71.2,76,78.8]
I4=[0,0.268,0.046,0.612,0.021,0.98,0.063,1.326,0.309,1.695,0.833,1.783,1.16]
V5=[8,17.4,22.6,28.4,34,40.2,45.8,50.4,57.8,65.2,70.6,78.6]
I5=[0,0.235,0.06,0.585,0.053,0.987,0.128,1.246,0.372,1.532,0.842,1.941]

plt.figure(dpi=200)
plt.title("$I_A-V_{G2K}$峰值峰谷曲线")
plt.xlabel("$V_{G2K}(V)$")
plt.ylabel("$I_A$(uA)")
plt.plot(V1,I1,".-",label="$V_F=2.0V,V_{G1K}=1.5V,V_{G2A}=7.0V")
plt.plot(V2,I2,".-",label="$V_F=2.2V,V_{G1K}=1.5V,V_{G2A}=7.0V")
plt.plot(V3,I3,".-",label="$V_F=1.8V,V_{G1K}=1.5V,V_{G2A}=7.0V")
plt.plot(V4,I4,".-",label="$V_F=2.0V,V_{G1K}=1.5V,V_{G2A}=7.5V")
plt.plot(V5,I5,".-",label="$V_F=2.0V,V_{G1K}=1.5V,V_{G2A}=6.5V")
plt.legend()

df=pd.read_excel(r"D:\zty\Documents\mypyproject\大学物理实验\frankdata.xlsx")
y=df[0]
x=df[8]
plt.figure(dpi=200)
plt.title("$I_A-V_{G2K}$曲线")
plt.xlabel("$V_{G2K}(V)$")
plt.ylabel("$I_A$(uA)")
plt.plot(x,y,"b.-",label="手动测量数据")
plt.legend()
peaks, _ = find_peaks(y, height=0.35, distance=11)
xp=[]
yp=[]
for peak in peaks:
    xp.append(x[peak])
    yp.append(y[peak])
#拟合求周期
[A,B],C=np.polyfit(range(len(xp)),xp,1,cov=True) 
# 计算每个参数的标准误差
errors = np.sqrt(np.diag(C))
print("斜率K={:.8g}±{:.8g}\n截距b={:.8g}±{:.8g}".format(A,errors[0],B,errors[1]))