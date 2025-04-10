#递归法
'''
以递归代替循环，循环变量可以参数传递，在循环中变化的量也以参数传递。
'''
def d(n,b1=1,b2=1):
    if n!=0:
        print(b1,end="," if n!=1  else '')
        b1,b2=b2,b1+b2
        d(n-1,b1,b2)  
#递推法
k=20
a1=1
a2=1
for i in range(k):
    print(a1,end="," if i!=k-1  else '')
    a1,a2=a2,a1+a2

##图像测试    

# 5 非线性函数拟合：样条函数拟合(Spline function)
import numpy as np
import matplotlib.pyplot as plt  # 导入 Matplotlib 工具包
from scipy.interpolate import UnivariateSpline  # 导入 scipy 中的样条插值工具
# 创建给定数据点集 (x,yObs)
# y = p0 + ((x*x-p1)**2+ p2) * np.sin(x*p3)
np.random.seed(1)
p0, p1, p2, p3 = [1.0, 1.2, 0.5, 0.8]  # 拟合函数的参数
x = np.linspace(-1, 2, 30)  # 生成已知数据点集的 x
y = p0 + ((x*x-p1)**2+ p2) * np.sin(x*p3)  # 生成理论值 y
yObs = y + 0.5*np.random.randn(x.shape[-1])  # 生成带有噪声的观测数据
# 由给定数据点集 (x,y) 求拟合函数的参数 fSpl
fSpl = UnivariateSpline(x, yObs)  # 三次样条插值，默认 s= len(w)
coeffs = fSpl.get_coeffs()  # Return spline coefficients
print("Data fitting with spline function")
print("coeffs of 3rd spline function:\n  ", coeffs)
# 由拟合函数 fitfunc 计算拟合曲线在数据点的函数值
yFit = fSpl(x)  # 由插值函数 fSpl1 计算插值点的函数值 yFit
# 对拟合函数 fitfunc 进行平滑处理
fSpl.set_smoothing_factor(10)  # 设置光滑因子 sf
yS = fSpl(x)   # 由插值函数 fSpl(sf=10) 计算插值点的函数值 ys
coeffs = fSpl.get_coeffs()  # 平滑处理后的参数
print("coeffs of 3rd spline function (sf=10):\n  ", coeffs)
# 绘图
fig, ax = plt.subplots(figsize=(8,6))
ax.set_title("Data fitting with spline function")
plt.scatter(x, yObs, label="observed data")
plt.plot(x, y, 'r--', label="theoretical curve")
plt.plot(x, yFit, 'b-', label="3rd spline fitting")
plt.plot(x, yS, 'm-', label="smoothing spline")
plt.legend(loc="best")
# Data fitting with spline function
# coeffs of 3rd spline function:
#    [-0.09707885  3.66083026 -4.20416235  7.95385344]
# coeffs of 3rd spline function (sf=10):
#    [0.41218039 0.52795588 1.6248287  0.76540737 8.49462738]
