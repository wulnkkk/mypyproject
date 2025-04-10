import pandas as pd ,numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.interpolate import make_interp_spline
plt.rcParams ['font.sans-serif'] = ['Simhei']
from scipy.stats import pearsonr
##数据处理
data0=pd.read_excel(r"D:\mypyproject\data\杨氏实验\experimentdata01.1.xlsx")  #数据存放路径
data0['tan(a-2n*theta)']=(data0['xn(mm)']-data0.loc[0,'dxn(mm)'])/data0['hn(mm)']
data0['2n*theta']=(data0.loc[0,'tan(a-2n*theta)']-data0['tan(a-2n*theta)'])/(1+data0.loc[0,'tan(a-2n*theta)']*data0['tan(a-2n*theta)'])
print(data0)




##回归分析
px=data0.index
py=data0['2n*theta']
fig=plt.figure(figsize=(15,5),dpi=120)
plt.scatter(px,py,color='b',label='.')
plt.xticks(np.arange(0,12))
plt.yticks(np.arange(0,0.005))
plt.xlabel('n')
plt.ylabel('2n*theta(rad)')
plt.title('角度测量数据2n*theta-n')
plt.grid()
r=pearsonr(data0.index,data0['2n*theta'])[0]#线性相关系数
print(r)
X=sm.add_constant(px)
model=sm.OLS(py,X)
results=model.fit()
x=np.linspace(px.min(),px.max(),100)
x=sm.add_constant(x)
y=results.predict(x)
plt.plot(x[:,1],y,'r',alpha=1)
plt.show()
print(results.summary())
print("Parameters: ", results.params)#斜率及截距
print("Standard errors: ", results.bse)#相应标准误差


#E的计算
m=0.0094*5
g=9.7915
L=0.215
a=0.025
b=0.025
d=data0.mean()['d(mm)']
dd=data0.loc[0,'dd(mm)']  ##游标卡尺零点
#theta2=results.params['x1']
theta2=data0['2n*theta']
E=12*m*g*(L-a/2)**2/(b*((d-dd)*0.001)**3*theta2)   ##点模型

#E=4*m*g/a/(theta2*b*((d-dd)*0.001)**3)*((L)**3-(L-a)**3) ##均匀分布模型
#print('{:.4e}'.format(E))
# print(E[1:])
# x=np.array([0,10,20,40,80,160,320])
# y=np.array(E[1:])
# x_new=np.linspace(min(x),max(x))
# y_smooth=make_interp_spline(x,y)(x_new)
# plt.scatter(x,y,c='b')
# plt.plot(x_new,y_smooth,c='red')
# plt.title('E-t')
# plt.xlabel('t(s)')
# plt.ylabel('E(Pa)')
# plt.show()