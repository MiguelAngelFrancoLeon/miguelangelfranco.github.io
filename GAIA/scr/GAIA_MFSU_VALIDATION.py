import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Constantes MFSU
CHI = 12.65
PAUSA_FRANCO = 0.921

def analizar_mfsu_gaia(path):
    df = pd.read_csv(path)
    
    # MATEMÁTICA REAL MFSU
    # Despejamos delta_F: Vobs = Vbar * CHI^(1-delta_F)
    df['delta_F_calculado'] = 1 - (np.log(df['v_obs_kms'] / df['v_bar_kms']) / np.log(CHI))
    
    # Guardar resultados procesados
    df.to_csv('resultados_mfsu_gaia.csv', index=False)
    
    # Resumen Estadístico
    mean_delta = df['delta_F_calculado'].mean()
    print(f"Análisis completado para {len(df)} eventos.")
    print(f"Valor medio de delta_F: {mean_delta:.4f}")
    print(f"Desviación respecto a la Pausa de Franco (0.921): {mean_delta - PAUSA_FRANCO:.4f}")
    
    return df

# Ejecutar
analisis = analizar_mfsu_gaia('gaia_massive_events.csv')
