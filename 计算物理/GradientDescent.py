#利用拉格朗日插值法进行函数拟合
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号

def fun(x,y):   #原函数
    f=x**2 +100*y**2 + 4
    return f

def dfun(x,y):  #导函数
    df=np.array([2*x,200*y])
    return df


dx=0.01   #步长
dy=0.01
x,y=[1,1] #初始点
f=fun(x,y)
f_list=[]
for i in range(102):
    f_list.append(f)
    df=dfun(x,y)
    if df[0]>0 and df[1]>0:
        x=x-dx
        y=y-dy
        f=fun(x,y)
    elif  df[0]<0 and df[1]>0:
        x=x+dx
        y=y-dy
        f=fun(x,y)
    elif df[0]>0 and df[1]<0:
        x=x-dx
        y=y+dy
        f=fun(x,y)
    else:
        x=x+dx
        y=y+dy
        f=fun(x,y)
print(f_list)