import numpy as np
import matplotlib.pyplot as plt

# Parámetros fundamentales
delta_F_0 = 0.921
impedance = 5.85
tortuosity = 2.22
# Usamos un factor de visualización para que el decaimiento sea visible en el gráfico
Rf_viz = 0.05 

n = np.arange(0, 40)
delta_F_n = delta_F_0 * (1 - Rf_viz)**n

plt.figure(figsize=(10, 6), dpi=300)

# Graficar curva (usando 'r' antes de los strings para evitar el SyntaxWarning)
plt.plot(n, delta_F_n, color='#1f77b4', linewidth=2.5, label='MFSU Dimensional Decay', zorder=1)

# Resaltar Punto Franco 0.921
plt.scatter(0, delta_F_0, color='red', s=150, edgecolors='black', zorder=5, label=f'Original Event (Branch 0): {delta_F_0}')

# Anotación profesional sin errores de sintaxis
plt.annotate(r'Primordial Seed $\delta_F = 0.921$', 
             xy=(0, delta_F_0), xytext=(8, 0.88),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
             fontsize=12, fontweight='bold')

# Marcar ramas secundarias
ramas = [5, 12, 25]
for r in ramas:
    plt.scatter(r, delta_F_n[r], color='orange', s=80, edgecolors='black', zorder=4)
    plt.text(r+1, delta_F_n[r]+0.02, f'Branch {r}', fontsize=10)

plt.title('Figure 1: Coherence Decay and Branching Hierarchy', fontsize=14, fontweight='bold')
plt.xlabel('Branching Generation (n)', fontsize=12)
plt.ylabel(r'Coherence Value ($\delta_F$)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right')
plt.ylim(0, 1.0)

plt.savefig('franco_curve.png', bbox_inches='tight')
plt.show()
