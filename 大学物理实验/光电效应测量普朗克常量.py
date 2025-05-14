import numpy as np                
import matplotlib.pyplot as plt   
import scipy.constants as Con
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号
a=np.array([x+9.8 for x in range(410,575,15)])
aa=3e17/a
U0=-np.array([1.73,1.62,1.56,1.43,1.35,1.26,1.19,1.11,1.04,0.98,0.91])
Ud=-np.array([1.73,1.64,1.60,1.46,1.36,1.28,1.20,1.12,1.06,1,0.92])
plt.figure(dpi=200)
plt.scatter(aa,U0,label="数据点")
#拟合
[A,B],C=np.polyfit(aa,U0,1,cov=True) 
# 计算每个参数的标准误差
errors = np.sqrt(np.diag(C))
print(A,B,errors)
y=lambda A,B,X : A*X+B
plt.plot(aa,y(A,B,aa),label="拟合曲线")
plt.title("$ U_0-v $曲线")
plt.xlabel("入射光频率(Hz)")
plt.ylabel("截止电压(V)")
plt.text(6e14,-1.18,"斜率K={:.8g}±{:.8g}\n截距b={:.8g}±{:.8g}".format(A,errors[0],B,errors[1]))
plt.legend()
plt.show()
print("h={:.8g}±{:.8g}\nw={:.8g}±{:.8g}".format(A*Con.e,errors[0]*Con.e,B*Con.e,errors[1]*Con.e))
plt.figure(dpi=200)
plt.scatter(aa,Ud,label="数据点")
#拟合
[A,B],C=np.polyfit(aa,Ud,1,cov=True) 
# 计算每个参数的标准误差
errors = np.sqrt(np.diag(C))
print(A,B,errors)
y=lambda A,B,X : A*X+B
plt.plot(aa,y(A,B,aa),label="拟合曲线")
plt.title("$ U_d-v $曲线")
plt.xlabel("入射光频率(Hz)")
plt.ylabel("截止电压(V)")
plt.text(6e14,-1.18,"斜率K={:.8g}±{:.8g}\n截距b={:.8g}±{:.8g}".format(A,errors[0],B,errors[1]))
plt.legend()
plt.show()
print("h={:.8g}±{:.8g}\nw={:.8g}±{:.8g}".format(A*Con.e,errors[0]*Con.e,B*Con.e,errors[1]*Con.e))


u1=[0,2,4,8,10,12,16,20,28,38,40,42,45,50]
i1=[0.5,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.5,1.5,1.5,1.5]
u2=[0,2,3,5,6,8,12,16,18,22,28,38,40,42,45,48,50]
i2=[0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.7,1.7,1.7,1.7]
u3=[0,2,3,5,8,10,14,18,22,26,30,38,40,45,48,50]
i3=[0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.6,1.6,1.6,1.6]
plt.figure(dpi=200)
plt.plot(u1,i1,'r.-',label="$\lambda$={:}nm".format(1009.8))
plt.plot(u2,i2,'b.-',label="$\lambda$={:}nm".format(909.8))
plt.plot(u3,i3,'y.-',label="$\lambda$={:}nm".format(809.8))
plt.legend()
plt.title("$ U_d-v $曲线")
plt.xlabel("栅极电压(v)")
plt.ylabel("光电流I($10^{-10}$A)")