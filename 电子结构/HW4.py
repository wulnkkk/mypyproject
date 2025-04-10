# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:15:53 2022

@author: Zeyu
liuzyspe@hnu.edu.cn

"""
import numpy as np
import matplotlib.pyplot as plt


a = 2*np.pi # 晶格常数
V0 = 2.0   # 可以自己调节大小
s = 2*np.pi #可以自己调节宽窄

#生成哈密顿量
def H(n=5,k=0,V0 = V0): #n, 取到第n个平面波
    G = np.arange(-n,n+1)*2*np.pi/a  #生成倒格矢
    diag_component = 1/2*(k+G)*(k+G) #对角线元素：纯粹的自由电子情况
    H_matrix = np.zeros([2*n+1,2*n+1]) #H矩阵初始化
    for i in range(2*n+1):
        H_matrix[i,i] = diag_component[i]/2 # 填入对角元素
        for j in range(i+1,2*n+1): # 对称矩阵，只需要填一半的矩阵内容
            n_ = (G[i] - G[j])*a/2/np.pi # 公式中的n值，对影成不同的倒格矢的差值
            H_matrix[i,j] = V0*a*s/(a**2*np.pi-4*n**2*np.pi*s**2)*np.cos((n_*np.pi*s/a))
            
    H_matrix = H_matrix + H_matrix.T # 把矩阵剩下一半填上
    return H_matrix

def Cal_E(H):
    return np.sort(np.linalg.eig(H)[0]) #计算特征值并从小到大排列

k_num = 30 # 离散化的k点数目
k = np.linspace(-np.pi/a, np.pi/a, k_num)
n_cut = 5   #n_cut, 取到第n_cut个平面波
band = np.zeros([k_num,2*n_cut+1]) # 储存计算得到的能带
band_free = np.zeros([k_num,2*n_cut+1]) # 储存计算得到的自由电子能带
for i in range(len(k)): #对每一个k点
    band[i,:]=Cal_E(H(n_cut,k[i])) #计算能带
    band_free[i,:] = Cal_E(H(n_cut,k[i],V0=0)) # 对应情况下的自由电子的能带

#画图，没有实际的内涵
plt.figure(dpi=300)

plt.plot(k,band_free[:,0],'r--',label = 'Free electron',linewidth=3)
plt.plot(k,band[:,0],'k',label = 'Periodic potential')
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
for i in range(1,8):
    plt.plot(k,band_free[:,i],'r--',label = 'Free electron',linewidth=3)
    plt.plot(k,band[:,i],'k',label = 'Periodic')
#拆成i=0和i大于0，只是为了标注


   
plt.gca().set_aspect(2/8) # 只是为了好看一些
plt.xticks(ticks=[-0.5,0.5],labels=[r'-$\pi/a$','$\pi/a$'])
plt.yticks([])
plt.ylim([-0.5,8])
plt.xlim([-0.5,0.5])
plt.plot([0,0],[-1,8],'--k')
