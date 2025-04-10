import pandas as pd ,numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm 
from scipy.optimize import curve_fit
from scipy.signal import find_peaks ,peak_widths
plt.rcParams ['font.sans-serif'] = ['Simhei']  #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号

f=pd.read_csv(r"D:\zty\Documents\mypyproject\现代实验\实验八宇宙线μ子平均寿命测量\μ子数据20241215_191437.csv",encoding="ANSI",header=5)

## 将两种数据分开
df1=pd.DataFrame()
df1["日期时间"]=np.array(f.loc[0:f[f["日期时间"]=="探测器角度"].index[0]-1,"日期时间"])
df1["μ子寿命"]=np.array(f.loc[0:f[f["日期时间"]=="探测器角度"].index[0]-1,"μ子寿命"])
df2=pd.DataFrame()
df2["探测器角度"]=np.array(f.loc[f[f["日期时间"]=="探测器角度"].index[0]+1:,"日期时间"])
df2["μ子通量计数（/s）"]=np.array(f.loc[f[f["日期时间"]=="探测器角度"].index[0]+1:,"μ子寿命"])

# plt.title(r"\mu子寿命谱")
# plt.xlabel("寿命(us)")
# plt.ylabel
# plt.ylabel("计数")
# plt.plot(f["μ子寿命"],)
# plt.show()
