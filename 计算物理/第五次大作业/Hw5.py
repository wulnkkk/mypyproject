import numpy as np
import matplotlib.pyplot as plt
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号


def initialize_spins(N):
    return np.random.choice([-1, 1], size=(N, N))

def calculate_energy(changes, J=1.0):
    return -J * np.sum(changes)

def metropolis_step(spins, temperature):
    N = spins.shape[0]
    i, j = np.random.randint(0, N, 2)
    old_spin = spins[i, j]
    new_spin = -old_spin
    neighbors = [spins[(i-1) % N, j], spins[(i+1) % N, j], spins[i, (j-1) % N], spins[i, (j+1) % N]]
    changes = np.array(neighbors) * new_spin
    delta_E = calculate_energy(changes)
    if delta_E < 0 or np.random.rand() < np.exp(-delta_E / temperature):
        spins[i, j] = new_spin
    return spins

def simulate(N, temperature, steps):
    spins = initialize_spins(N)
    for _ in range(steps):
        spins = metropolis_step(spins, temperature)
    return spins

def calculate_magnetization(spins):
    return np.sum(spins) / spins.size

def run_simulation(N, temperatures, steps_per_temp, steps_per_measurement):
    magnetizations = []
    magnetization_squared = []
    for T in temperatures:
        mag_sum = 0
        mag_sum_squared = 0
        for _ in range(steps_per_measurement):
            spins = simulate(N, T, steps_per_temp)
            mag = calculate_magnetization(spins)
            mag_sum += mag
            mag_sum_squared += mag ** 2
        magnetizations.append(mag_sum / steps_per_measurement)
        magnetization_squared.append(mag_sum_squared / steps_per_measurement)
    return magnetizations, magnetization_squared

# Parameters
N = 10
temperatures = np.linspace(0.1, 4.0, 20)
steps_per_temp = 1000
steps_per_measurement = 100

# Run simulation
magnetizations, magnetization_squared = run_simulation(N, temperatures, steps_per_temp, steps_per_measurement)

# Calculate fluctuations
fluctuations = magnetization_squared - np.array(magnetizations) ** 2

# Plot results
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(temperatures, magnetizations, label='Magnetization')
plt.xlabel('Temperature')
plt.ylabel('Magnetization')
plt.title('Magnetization vs Temperature')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(temperatures, fluctuations, label='Fluctuations', color='orange')
plt.xlabel('Temperature')
plt.ylabel('Fluctuations')
plt.title('Fluctuations vs Temperature')
plt.legend()

plt.tight_layout()
plt.show()
