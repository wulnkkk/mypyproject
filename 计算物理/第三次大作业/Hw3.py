import numpy as np
import matplotlib.pyplot as plt
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号


# 参数设置
L = 1.0       # 杆的长度
T = 0.1       # 总时间
Nx = 10       # 空间步数
Nt = 100      # 时间步数
alpha = 0.835 # 热扩散系数

# 计算空间和时间步长
dx = L / Nx
dt = T / Nt

# 稳定性条件
r = alpha * dt / (dx ** 2)
assert r < 0.5, "稳定性条件不满足，请减小时间步长dt或空间步长dx"

# 初始化温度分布
x = np.linspace(0, L, Nx+1)
T = np.zeros((Nt+1, Nx+1))
T[0, :] = 100 * np.ones(Nx+1)  # 初始温度分布

# 边界条件
T[:, 0] = 0
T[:, -1] = 100

# Crank-Nicolson方法
A = (1 + 2*r) * np.eye(Nx-1) - r * np.eye(Nx-1, k=-1) - r * np.eye(Nx-1, k=1)
B = (1 - 2*r) * np.eye(Nx-1) + r * np.eye(Nx-1, k=-1) + r * np.eye(Nx-1, k=1)

for n in range(0, Nt):
    T[n+1, 1:-1] = np.linalg.solve(A, np.dot(B, T[n, 1:-1]))

# 绘制结果
plt.figure(figsize=(10, 6))
for n in range(0, Nt+1, Nt//5):
    plt.plot(x, T[n, :], label=f't={n*dt:.2f}s')
plt.xlabel('Position (x)')
plt.ylabel('Temperature (T)')
plt.title('Temperature distribution along the rod over time')
plt.legend()
plt.show()
