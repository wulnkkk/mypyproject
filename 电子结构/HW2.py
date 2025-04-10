# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eig as Eig #用来计算广义特征值

def Psi(x, a = 13):
    y = np.exp(-a*np.power(x,2))
    return y
#定义基函数

def S_matrix(a):
    S = np.zeros([4,4])
    for i in range(4):
        for j in range(4):
            temp = np.pi/(a[i]+a[j])
            S[i,j] = np.power(temp,3/2)
    return S

def T_matrix(a):
    T = np.zeros([4,4])
    for i in range(4):
        for j in range(4):
            temp = 3*a[i]*a[j]*np.power(np.pi,3/2)/(np.power((a[i]+a[j]),5/2))
            T[i,j] = temp 
    return T

def V_matrix(a):
    A = np.zeros([4,4])
    for i in range(4):
        for j in range(4):
            A[i,j] = -2*np.pi/(a[i]+a[j])
    return A
#广义特征值问题求解器
def Equation_solver(F):
    e_val = Eig(F,S)[0]
    e_state = Eig(F,S)[1]
    idx = e_val.argsort()
    e_val = e_val[idx]
    e_state = e_state[:,idx][:,0] # 只保留最低特征值的特征向量，这一点和之前不一样
    #factor = 1/np.sqrt(np.einsum('pl,pq,ql -> l',e_state,S,e_state))
    factor = 1/np.sqrt(e_state.dot(S).dot(e_state)) #归一化
    e_state = factor*e_state
    return e_state # 只输出特征向量，不再输出特征值了

def cal_basis(x,a):
    basis_ = np.zeros([len(x_),len(a)])
    for i in range(len(a)):
        basis_[:,i] = Psi(x,a[i])
    return basis_
a = [13.00773, 1.962079,0.444529,0.1219492]
S = S_matrix(a)
H = T_matrix(a)+V_matrix(a)


#计算能量，因为这里特征值不再是体系的能量
def Cal_totalE(C):
    E =  np.einsum('p,q,pq',C,C,H) 
    return E

    
#初始设置,全部权重都是1，我们可以随意试验不同的初始条件
#C = np.squeeze(np.ones([4,1]))
#更换初始条件
C = np.array([0,0,0,0])
# 对初始条件归一化
#C = 1/np.sqrt(C.dot(S).dot(C))*C
#第0步计算
F = H  # 生成Fock矩阵
C = Equation_solver(F) # 计算特征向量 或者说是氦原子轨道
E = Cal_totalE(C) # 计算体系能量

i = 1
E_list = [E]

#迭代开始， scf过程
while (i<20): # At most 20 iteration
    F = H 
    i = i + 1
    E_old = E
    C = Equation_solver(F)
    E = Cal_totalE(C)
    #print(E)
    E_list.append(E)
    if abs(E-E_old)<1e-12: # 收敛判断，一个比较随意的收敛判据
        break # 退出循环过程

print('Total energy: '+ str(E) + ' after ' + str(i) + ' iteration')
plt.figure(dpi=300)
plt.plot(E_list,marker = '*',color='r')
plt.xlim([0,10])
#plt.ylim([-2.856,-2.840])
plt.xlabel('Iteration index',fontsize=18)
plt.ylabel('Energy (Hartree)',fontsize=18)
plt.show()    

##画出基态波函数
x_=np.linspace(0,2,1000)
basis_=cal_basis(x_,a)
res = abs(basis_.dot(C)) #使用矩阵乘法简化计算
plt.figure(dpi=300)
plt.ylabel("Wavefunction")
plt.xlabel(r"$r(a_0)$")
plt.plot(x_,2/np.sqrt(4*np.pi)*np.exp(-x_),color='r',label='true')
plt.plot(x_,res,'--b',label = 'approximated') # for normalization purpose
plt.legend()
plt.show()

