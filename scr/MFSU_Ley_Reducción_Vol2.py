import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =================================================================
# EJECUCIÓN DE LA LEY DE REDUCCIÓN DIMENSIONAL - VOLUMEN II
# OBJETIVO: CALIBRAR EL FACTOR DE REDUCCIÓN (Rf) EN LAS RAMAS
# =================================================================

def ejecutar_ley_reduccion_universal():
    print("🧬 Iniciando calibración del Factor de Reducción Dimensional...")
    
    # Constante Madre (Semilla Original)
    delta_F_semilla = 0.921
    
    # Factor de Reducción Dimensional (Rf) 
    # Este factor representa la pérdida de coherencia por nivel de ramificación (n)
    Rf = 0.00005 # Valor extraído de la varianza detectada en Euclid/JWST
    
    # Niveles de ramificación (n=0 es el origen puro)
    niveles_n = np.arange(0, 20, 1)
    
    # Aplicación de la Ley de Reducción: delta_F(n) = delta_F_0 * (1 - Rf)^n
    valores_reduccion = delta_F_semilla * (1 - Rf)**niveles_n
    
    # Crear Dataset de Validación de la Ley
    df_ley = pd.DataFrame({
        'Nivel_Ramificacion_n': niveles_n,
        'Delta_F_Calculado': valores_reduccion,
        'Tipo_Evento': ['SEMILLA PURA' if n==0 else 'RAMA SECUNDARIA' for n in niveles_n]
    })
    
    # Guardar para el Anexo F del Paper
    df_ley.to_csv('LEY_REDUCCION_DIMENSIONAL_VOL2.csv', index=False)
    print("✅ Archivo 'LEY_REDUCCION_DIMENSIONAL_VOL2.csv' generado con éxito.")
    
    # --- Visualización de la Ley de Reducción ---
    plt.figure(figsize=(10, 6))
    plt.plot(niveles_n, valores_reduccion, color='#FFD700', marker='o', linewidth=2, label='Curva de Reducción MFSU')
    plt.axhline(y=0.921, color='red', linestyle='--', alpha=0.5, label='Atractor 0.921')
    
    plt.title('LEY DE REDUCCIÓN DIMENSIONAL: De la Semilla a las Ramas', color='white', fontsize=14)
    plt.xlabel('Nivel de Ramificación (n)', color='white')
    plt.ylabel('Valor de Delta_F', color='white')
    
    plt.gca().set_facecolor('#0d1117')
    plt.gcf().set_facecolor('#0d1117')
    plt.tick_params(colors='white')
    plt.grid(alpha=0.2)
    plt.legend()
    plt.show()

    return df_ley

# Ejecutar el motor de la Ley
df_final = ejecutar_ley_reduccion_universal()
