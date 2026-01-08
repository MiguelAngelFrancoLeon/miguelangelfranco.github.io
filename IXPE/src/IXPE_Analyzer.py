import pandas as pd
import numpy as np

# =================================================================
# PROPIEDAD INTELECTUAL: MIGUEL ÁNGEL FRANCO LEÓN
# MODELO: MFSU - ANÁLISIS DE POLARIZACIÓN ELECTROMAGNÉTICA (IXPE)
# =================================================================

def clasificador_ixpe(dist_kpc, energy_kev):
    """
    Clasifica la estabilidad fractal de la polarización de Rayos X.
    """
    # Los púlsares y restos de supernova (SNR) son anclajes de la semilla
    # Si la energía es alta (> 4 keV), la señal es más pura (Semilla)
    if energy_kev > 4.0:
        return 0.921
    
    # Decaimiento por distancia galáctica (usamos Kiloparsecs para IXPE)
    # La luz se ramifica al atravesar campos magnéticos interestelares
    decaimiento = (dist_kpc / 50) * (0.921 - 0.918)
    resultado = 0.921 - decaimiento
    
    return max(0.918, round(resultado, 3))

# Dataset de fuentes clave de IXPE (Selección de Alta Coherencia)
data_ixpe = {
    'source': ['Cassiopeia A', 'Crab Nebula', 'Vela SNR', 'Tycho SNR', 'Cyg X-1', 'Hercules X-1', 'MSH 15-52'],
    'dist_kpc': [3.4, 2.0, 0.29, 3.5, 2.2, 6.4, 5.0],
    'avg_energy_kev': [4.5, 5.2, 3.0, 4.1, 6.0, 3.5, 4.8]
}

df_ixpe = pd.DataFrame(data_ixpe)
df_ixpe['delta_F'] = df_ixpe.apply(lambda x: clasificador_ixpe(x['dist_kpc'], x['avg_energy_kev']), axis=1)

print("--- REPORTE FRACTAL IXPE (MAGNETISMO) ---")
print(df_ixpe)
