import matplotlib.pyplot as plt
import numpy as np

# Datos extraídos (SPARC + JWST)
redshifts = [0, 0, 2.1, 4.5, 7.2, 9.1, 10.6, 11.4, 12.1]
delta_f_values = [0.921, 0.919, 0.850, 0.780, 0.720, 0.684, 0.637, 0.604, 0.582]

def plot_fractal_evolution():
    plt.figure(figsize=(10, 6), facecolor='#0a0a0c')
    ax = plt.gca()
    ax.set_facecolor('#0a0a0c')
    
    # Curva de tendencia MFSU
    z_line = np.linspace(0, 13, 100)
    # Ley de Franco: La saturación decae logarítmicamente con la distancia
    f_line = 0.921 * np.exp(-0.04 * z_line) 
    
    plt.plot(z_line, f_line, color='#00d4ff', label='Predicción MFSU V2', alpha=0.6)
    plt.scatter(redshifts, delta_f_values, color='#ff00ff', s=100, label='Galaxias Reales (SPARC/JWST)')
    
    plt.title('Evolución de la Saturación Fractal (${\delta}_F$)', color='white', fontsize=14)
    plt.xlabel('Redshift (z) - Distancia al Origen', color='white')
    plt.ylabel('Constante de Saturación ${\delta}_F$', color='white')
    plt.legend()
    plt.grid(color='#333', linestyle='--')
    plt.savefig('EVOLUCION_FRACTAL_Z.png')
    plt.show()

# Ejecutar para ver la prueba
# plot_fractal_evolution()
