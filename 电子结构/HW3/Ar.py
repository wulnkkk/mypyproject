# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 14:36:22 2022

@author: Zeyu
"""

import numpy as np
from scipy.linalg import eig as Eig #用来计算广义特征值
import matplotlib.pyplot as plt

# 读取各种矩阵
S = np.loadtxt('S_matrix')
T = np.loadtxt('T_matrix')
V_ne = np.loadtxt('V_nuclei_matrix')
nao = len(S) # 查看用了多少个基组函数，或者整个计算的维度
V = np.loadtxt('V_matrix').reshape([nao,nao,nao,nao])

# 对下一行输入的物理信息填空
nelec = 18  # Number of electron is ? in Ar


def Equation_solver(F,S): # 广义特征值求解器
    e_val,e_state = Eig(F,S) # 求解特征值 eigenvalue
    idx = e_val.argsort() #对特征值从小到大进行排列
    e_val = e_val[idx] #排列特征值
    e_state = e_state[:,idx] # 排列特征向量
    #下面计算归一化因子factor
    factor = 1/np.sqrt(np.einsum('pl,pq,ql -> l',e_state,S,e_state))
    e_state = factor*e_state
    e_val = np.real(e_val)
    return e_val,e_state #返回特征值与特征向量，这里特征值是各个态的能量

def cal_new_dm(dm): # scf过程，获得新的电荷密度
    J = np.einsum('rs,pqrs->pq', dm, V)
    K = -1/2 * np.einsum('rs,prqs->pq', dm, V)
    F = T + V_ne + J + K
    eigs, coeffs = Equation_solver(F, S)
    coeff_occupied = coeffs[:, :int(nelec / 2)]
    dm = 2 * np.einsum('pi,qi -> pq', coeff_occupied, coeff_occupied)
    return dm ,F # 返回新的密度矩阵和Fork矩阵

def hf_energy(dm): # 能量计算，不同的电荷密度有不同的体系能量
    J = np.einsum('rs,pqrs->pq',dm,V)
    K = -1/2*np.einsum('rs,prqs->pq',dm,V)
    E_1 = np.einsum('pq,pq',T + V_ne,dm)
    E_2 = np.einsum('pq,pq',J + K,dm)
    return E_1+E_2



def orital_energy_calculator(F,S):
    # 填入轨道能量计算器
    eigs, _ = Equation_solver(F, S)
    idx = eigs.argsort() #对特征值从小到大进行排列
    eigs = eigs[idx] #排列特征值
    return eigs[:int(nelec / 2)]

# 主循环
dm = np.zeros([nao, nao])  # 初始猜测
E = hf_energy(dm)
E_list = [E]

i = 1
while i < 100:  # 最多 100 次迭代
    E_old = E
    dm, F = cal_new_dm(dm)  # 获取新的密度矩阵和 Fock 矩阵
    E = hf_energy(dm)
    E_list.append(E)
    i += 1
    if abs(E - E_old) < 1e-10:  # 放宽收敛标准
        break

# 输出结果
plt.figure(dpi=200)
plt.plot(E_list[1:], '-*r')
plt.xlabel('# of Iteration', fontsize=18)
plt.ylabel('Energy (Hartree)', fontsize=18)
print('The converged energy is {0:.4f} Hartree after {1} iterations'.format(E_list[-1], i))
print(orital_energy_calculator(F, S))  # 使用 Fock 矩阵计算轨道能量