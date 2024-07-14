import numpy as np
import matplotlib.pyplot as plt

# Parameter
m = 1.0  # massa (kg)
F = 1.0  # gaya (N)
a = F / m  # percepatan (m/s^2)
t0 = 0.0  # waktu awal (s)
tf = 10.0  # waktu akhir (s)
dt = 0.01  # langkah waktu (s)
n_steps = int((tf - t0) / dt)  # jumlah langkah waktu

# Inisialisasi array untuk menyimpan hasil
t = np.linspace(t0, tf, n_steps)
x = np.zeros(n_steps)
v = np.zeros(n_steps)

# Kondisi awal
x[0] = 0.0
v[0] = 0.0

# Metode Euler
for i in range(1, n_steps):
    v[i] = v[i-1] + a * dt
    x[i] = x[i-1] + v[i-1] * dt

# Plot hasilnya
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x, label='Posisi (x)')
plt.xlabel('Waktu (s)')
plt.ylabel('Posisi (m)')
plt.title('Posisi vs. Waktu')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, v, label='Kecepatan (v)', color='orange')
plt.xlabel('Waktu (s)')
plt.ylabel('Kecepatan (m/s)')
plt.title('Kecepatan vs. Waktu')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
