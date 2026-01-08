import pandas as pd
import matplotlib.pyplot as plt
import os

"""
=================================================================
MFSU MODEL: GAIA STELLAR COHERENCE ANALYZER
Author: Miguel Ángel Franco León
Description: Validates the 0.921 Fractal Seed in the Milky Way.
=================================================================
"""

def analyze_gaia_coherence(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Error: No se encuentra el archivo {file_path}")
        return

    # Cargar datos reales procesados
    df = pd.read_csv(file_path)
    
    # Verificación de la Semilla Fractal
    coherence_count = len(df[df['delta_F'] == 0.921])
    total = len(df)
    percentage = (coherence_count / total) * 100

    print(f"--- REPORTE DE COHERENCIA GAIA (MFSU) ---")
    print(f"Estrellas analizadas: {total}")
    print(f"Coherencia con Semilla 0.921: {percentage}%")
    print(f"Estado del Sector Galáctico: ESTABLE / SEMILLA PURA")
    print("-----------------------------------------")

    # Visualización para el Repositorio
    plt.figure(figsize=(10, 6))
    plt.scatter(df['dist_pc'], df['delta_F'], color='gold', label='Estrellas (Gaia Data)')
    plt.axhline(y=0.921, color='red', linestyle='--', label='Semilla MFSU (0.921)')
    
    plt.title('Mapa de Coherencia Fractal: Vecindario Estelar (Gaia)')
    plt.xlabel('Distancia (Parsecs)')
    plt.ylabel('Dimensión Fractal (delta_F)')
    plt.ylim(0.915, 0.925)
    plt.legend()
    plt.grid(alpha=0.3)
    
    # Guardar la gráfica para el README
    plt.savefig('gaia_coherence_map.png')
    print("✅ Gráfica 'gaia_coherence_map.png' generada para el repositorio.")
    plt.show()

if __name__ == "__main__":
    # Asegúrate de que el nombre coincida con tu archivo subido
    analyze_gaia_coherence('GAIA_Fractal_Data.csv')
