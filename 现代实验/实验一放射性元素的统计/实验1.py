import pandas as pd ,numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm
plt.rcParams ['font.sans-serif'] = ['Simhei']
df=pd.read_excel(r"C:\Users\zty\Desktop\通道二.xlsx")
anum=dict()
for i in df["计数"]:
    if i not in anum.keys():
        anum[i]=1
    else:
        anum[i]+=1
print(anum)
xx=plt.figure(1)
plt.title("高斯计数本底")
plt.bar(anum.keys(),[x/sum(anum.values()) for x in anum.values()],label="测量数据")
ave=np.average(df["计数"])
def fun1(N):
    w=ave**N/math.factorial(N)*math.exp(-ave)
    return w
def fun2(N):
    w=1/(math.sqrt(2*math.pi*ave))*math.exp(-(N-ave)**2/2/ave)
    return w
plt.plot(sorted(anum.keys()),[fun1(x) for x in sorted(anum.keys())],"r--",label="泊松分布理论曲线")
plt.plot(sorted(anum.keys()),[fun2(x) for x in sorted(anum.keys())],"b-",label="高斯分布理论曲线")
plt.legend()
plt.show()