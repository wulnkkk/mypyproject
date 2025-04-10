import numpy as np
import matplotlib.pyplot as plt
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号
# 设定N的取值
N_values=range(0,10000,500)

# 进行实验
Std_list=[]
for N in N_values:
    # 每组实验的样本数为N，进行N组实验
    group_means = np.mean(np.random.normal(loc=0, scale=1, size=(N, N)), axis=1)
    # 计算这些均值的标准差
    std_of_means = np.std(group_means)
    Std_list.append(std_of_means)
# 作出实验结果与理论值的差距
Std_theory=np.array([1/np.sqrt(i) for i in N_values])
plt.xlabel(r"理论值 $\frac{1}{\sqrt{N}}$")
plt.ylabel("实验值")
plt.plot(Std_theory,Std_theory,'b--',label="理论曲线")
plt.scatter(Std_theory,Std_list,18,'r',"*")
plt.plot(Std_theory,Std_list,'r--',label="实验曲线")
plt.legend()


plt.xlabel("实验次数")
plt.ylabel("实验值与理论值的差")
plt.xticks(range(1,len(Std_theory-Std_list)+1),range(1,len(Std_theory-Std_list)+1))
plt.plot(range(1,len(Std_theory-Std_list)+1),Std_theory-Std_list)
plt.show()