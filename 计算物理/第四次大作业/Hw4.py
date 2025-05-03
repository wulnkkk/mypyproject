import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号

# 定义问题参数
n = 10  # 网格划分数量
L = 1.0  # 区间长度
h = L / (n + 1)  # 网格间距
x = np.linspace(0, L, n + 2)  # 网格点

# 定义源项 rho(x)
def rho(x):
    return 0.25 * np.pi * np.sin(np.pi * x)

# 定义精确解 phi_exact(x)
def phi_exact(x):
    return np.sin(np.pi * x)

# 组装刚度矩阵 A
# 对于线性基函数，A 的非零元素是 2/h 对角线和 -1/h 上下对角线
main_diag = 2 / h * np.ones(n)
off_diag = -1 / h * np.ones(n - 1)
A = diags([main_diag, off_diag, off_diag], [0, -1, 1]).tocsc()

# 组装载荷向量 d
d = np.zeros(n)
for i in range(n):
    d[i] = 4 * np.pi * (rho(x[i]) + rho(x[i + 1])) / 2 * h

# 求解线性方程组 A * a = d
a = spsolve(A, d)

# 构造数值解
phi_numerical = np.zeros(n + 2)
phi_numerical[1:-1] = a

# 计算精确解
phi_exact_values = phi_exact(x)

# 绘制数值解与精确解的对比图
plt.figure(figsize=(10, 6))
plt.plot(x, phi_numerical, 'r-o', label='数值解')
plt.plot(x, phi_exact_values, 'b--', label='精确解')
plt.xlabel('x')
plt.ylabel('$\Phi$')
plt.title('数值解与精确解的对比(网格数量n={})'.format(n))
plt.legend()
plt.grid(True)
plt.savefig('numerical_vs_exact_solution.png')
plt.show()

# 误差分析
error = np.linalg.norm(phi_numerical - phi_exact_values) / np.sqrt(n + 2)
print(f'均方差: {error:.10e}')

# 绘制误差随网格划分数量变化的趋势
errors = []
n_values = [5, 10, 20, 40, 80]
for n in n_values:
    h = L / (n + 1)
    x = np.linspace(0, L, n + 2)
    main_diag = 2 / h * np.ones(n)
    off_diag = -1 / h * np.ones(n - 1)
    A = diags([main_diag, off_diag, off_diag], [0, -1, 1]).tocsc()
    d = np.zeros(n)
    for i in range(n):
        d[i] = 4 * np.pi * (rho(x[i]) + rho(x[i + 1])) / 2 * h
    a = spsolve(A, d)
    phi_numerical = np.zeros(n + 2)
    phi_numerical[1:-1] = a
    phi_exact_values = phi_exact(x)
    error = np.linalg.norm(phi_numerical - phi_exact_values) / np.sqrt(n + 2)
    errors.append(error)

plt.figure(figsize=(10, 6))
plt.plot(n_values, errors, 'r-o', label='均方差')
plt.xlabel('网格划分数量 n')
plt.ylabel('均方差$sigma$')
plt.title('误差随网格划分数量变化的趋势')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.savefig('error_vs_mesh_size.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(np.log(n_values), np.log(errors), 'r-o', label='均方差')
plt.xlabel('网格划分数量的对数 ln(n)')
plt.ylabel('均方差的对数$ln(\sigma)$')
plt.title('误差随网格划分数量变化的趋势')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.savefig('error_vs_mesh_size1.png')
plt.show()