import numpy as np
import matplotlib.pyplot as plt
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文 
plt.rcParams['axes.unicode_minus'] = False # 显示负号

L=np.array([19.15,19.87,20.45,21.20,21.9,22.5,23.21,23.81,24.5,25.18])
n=np.arange(len(L))
#拟合
[A,B],C=np.polyfit(n,L,1,cov=True) 
# 计算每个参数的标准误差
errors = np.sqrt(np.diag(C))
print(A,B,errors)
y=lambda A,B,X : A*X+B
#作图
plt.figure(dpi=200)
plt.title("焦利称的定标")
plt.xlabel("砝码个数n")
plt.ylabel('弹簧末端的位置L(cm)')
plt.scatter(n,L,10,label="测量数据")
plt.plot(n,y(A,B,n),label="拟合曲线")
plt.legend()
plt.text(0,24,"拟合函数：y=A*x+B\n拟合参数：A={:.3f}$\pm${:.3f}\n  B={:.3f}$\pm${:.3f}".format(A,errors[0],B,errors[1]) )