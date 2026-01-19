import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Configuración de la semilla fractal y tortuosidad
delta_F_0 = 0.921
tau = 2.22
steps = 100 # Aumentamos puntos para una curva suave en 10 frames principales

# Generar una trayectoria tortuosa en una esfera (espacio de cuaterniones)
t = np.linspace(0, 10, steps)
x = np.sin(t/tau) * np.cos(t)
y = np.cos(t/tau) * np.sin(t)
z = np.linspace(1, delta_F_0, steps) # El eje Z representa el decaimiento de coherencia

fig = plt.figure(figsize=(10, 8), dpi=300)
ax = fig.add_subplot(111, projection='3d')

# Graficar la trayectoria (Camino Tortuoso)
ax.plot(x, y, z, color='#ff7f0e', linewidth=2.5, label=f'Tortuous Path (τ={tau})')

# Resaltar los 10 marcos de tiempo (time frames) mencionados en el paper
indices = np.linspace(0, steps-1, 10, dtype=int)
ax.scatter(x[indices], y[indices], z[indices], color='black', s=40, label='Time Frames (n)')

# Marcar el punto de origen (Evento Primordial)
ax.scatter(x[0], y[0], z[0], color='red', s=100, label='Primordial Branch (0.921)')

# Configuración de estilo
ax.set_title('Figure 3: Quaternion Trajectory & Coherence Decay', fontsize=14, fontweight='bold')
ax.set_xlabel('Quaternion i', fontsize=10)
ax.set_ylabel('Quaternion j', fontsize=10)
ax.set_zlabel('Coherence ($\delta_F$)', fontsize=10)

# Ajustar la vista para que sea profesional
ax.view_init(elev=20, azim=45)
ax.legend()

plt.savefig('quaternion_trajectory.png', bbox_inches='tight')
plt.show()
