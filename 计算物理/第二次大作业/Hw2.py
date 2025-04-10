import numpy as np
import matplotlib.pyplot as plt
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号

#解析解
def fun(x): 
    y=-4/(9/5*np.exp(-2*x)+2*x-1)
    return y

#原微分方程
def fun1(x,y):  
    dy=x*y**2+2*y
    return dy

#隐式欧拉法的迭代式
def fun2(x_k,y_k,h,err=1e-5):  
    n=1       #迭代求解y_k，n为迭代次数
    y_j=y_k   #赋值给牛顿迭代的迭代变量
    y_old=y_j  #用于判断收敛
    part1=y_j**2+(2*h-1)/(h*(x_k+h))*y_j+1/(h*(x_k+h))*y_k #注意，x_k与y_k在迭代过程中不变
    part2=2*y_j+(2*h-1)/(h*(x_k+h))
    y_j=y_j-part1/part2
    while abs(y_j-y_old)>err:  
        n=n+1
        y_old=y_j
        part1=y_j**2+(2*h-1)/(h*(x_k+h))*y_j+1/(h*(x_k+h))*y_k 
        part2=2*y_j+(2*h-1)/(h*(x_k+h))
        y_j=y_j-part1/part2
    # print("经过{:.5f}次迭代，{:.5f}对应的y值为{:.5f}".format(n,x_k+h,y_j))
    return y_j
#四阶龙格-库塔公式
def fun3(x_k,y_k,h):
    k1=fun1(x_k,y_k)
    k2=fun1(x_k+h/2,y_k+h*k1/2)
    k3=fun1(x_k+h/2,y_k+h*k2/2)
    k4=fun1(x_k+h,y_k+h*k3)
    y_k=y_k+h*(k1+2*k2+2*k3+k4)/6
    return y_k


#解析解
def realV(x_0,y_0,h): #函数化方便调用
    X=[x_0]
    Y=[y_0]
    x_i=x_0
    y_i=y_0
    while (x_i)<5:
        x_i=x_i+h               #自变量迭代放前面
        y_i=fun(x_i)            #解析解的公式
        X.append(x_i)
        Y.append(y_i)
    return X ,Y

#显式欧拉法
def V1(x_0,y_0,h):  #函数化方便调用
    X1=[x_0]
    Y1=[y_0]
    x_i=x_0
    y_i=y_0
    while (x_i)<5:
        y_i=y_i+h*fun1(x_i,y_i) #显式欧拉法的迭代式
        x_i=x_i+h               #自变量迭代放后面
        X1.append(x_i)
        Y1.append(y_i)
    return X1,Y1

#隐式欧拉法
def V2(x_0,y_0,h):  #函数化方便调用
    X2=[x_0]
    Y2=[y_0]
    x_i=x_0
    y_i=y_0
    while (x_i)<5:
        y_i=fun2(x_i,y_i,h,1e-10) #隐式欧拉法的迭代式
        x_i=x_i+h                 #自变量迭代放后面
        X2.append(x_i)
        Y2.append(y_i)
    return X2, Y2

#龙格-库塔法
def V3(x_0,y_0,h):  #函数化方便调用
    X3=[x_0]
    Y3=[y_0]
    x_i=x_0
    y_i=y_0
    while (x_i)<5:
        y_i=fun3(x_i,y_i,h)     #龙格-库塔法的迭代式
        x_i=x_i+h               #自变量迭代放后面
        X3.append(x_i)
        Y3.append(y_i)
    return X3, Y3

#初始值与步长
x_0=0
y_0=-5
h=0.1
X,Y=realV(x_0,y_0,h)
X1,Y1=V1(x_0,y_0,h)
X2,Y2=V2(x_0,y_0,h)
X3,Y3=V3(x_0,y_0,h)
#作图
plt.plot(X1,Y1,color="b",marker="^",markersize=3.5,label="显式欧拉法")  
plt.plot(X2,Y2,color="y",marker="v",markersize=3.5,label="隐式欧拉法")  
plt.plot(X3,Y3,color="g",marker="D",markersize=3.5,label="龙格-库塔法")  
plt.plot(X,Y,color="r",marker="o",markersize=3.5,label="解析解")
plt.legend()
plt.show()

#改变步长求误差
H=np.arange(0.01,5.01,0.01)
errlist1=[]
errlist2=[]
errlist3=[]
for h in H:
    X,Y=np.array(realV(x_0,y_0,h))
    X1,Y1=np.array(V1(x_0,y_0,h))
    X2,Y2=np.array(V2(x_0,y_0,h))
    X3,Y3=np.array(V3(x_0,y_0,h))
    err1=np.sqrt(np.mean((Y1-Y)**2))
    err2=np.sqrt(np.mean((Y2-Y)**2))
    err3=np.sqrt(np.mean((Y3-Y)**2))
    # print("步长为{:}时，显式欧拉法的均方差为{:.5f}".format(h,err1))
    # print("步长为{:}时，隐式欧拉法的均方差为{:.5f}".format(h,err2))
    # print("步长为{:}时，龙格-库塔法的均方差为{:.5f}".format(h,err3))
    if err1>10:  #对于误差大于10的步长,认为其不收敛，统一计为10
        err1=10
    if err2>10:
        err2=10
    if err3>10:
        err3=10
    errlist1.append(err1)
    errlist2.append(err2)
    errlist3.append(err3)

plt.plot(H,errlist1,color="b",marker="^",markersize=2,label="显式欧拉法")  
plt.plot(H,errlist2,color="y",marker="v",markersize=2,label="隐式欧拉法")  
plt.plot(H,errlist3,color="g",marker="D",markersize=2,label="龙格-库塔法")  
plt.legend()
plt.show()