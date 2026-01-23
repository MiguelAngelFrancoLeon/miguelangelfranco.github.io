import numpy as np
import pandas as pd
import math
import os

# --- MOTOR DIAMANTE (Lógica Pura) ---
def apply_mfsu_diamond(v_newtonian, n=0):
    CHI = 12.65
    DELTA_F = 0.921
    RU = 0.079
    FRACTAL_SCALE = 1.7418
    
    # Coherencia según la rama (n=0 para Original)
    coherence = DELTA_F * math.exp(-RU * n)
    # Boost estructural por Impedancia
    structural_boost = (CHI / (CHI - 1)) 
    
    # Proyección Final
    return v_newtonian * structural_boost * FRACTAL_SCALE

# --- DATA REAL (Muestra de SPARC para el repositorio) ---
# En un entorno de producción, aquí cargarías el archivo completo de SPARC
data_sparc = [
    {'name': 'M33',      'v_gas': 50.2, 'v_stars': 24.8, 'v_bulge': 0, 'v_obs': 105.4},
    {'name': 'NGC 2403', 'v_gas': 71.3, 'v_stars': 40.5, 'v_bulge': 0, 'v_obs': 134.0},
    {'name': 'UGC 128',  'v_gas': 102.0, 'v_stars': 35.0, 'v_bulge': 0, 'v_obs': 160.0},
    {'name': 'NGC 3198', 'v_gas': 92.4,  'v_stars': 34.2, 'v_bulge': 0, 'v_obs': 150.0},
    {'name': 'IC 2574',  'v_gas': 51.5,  'v_stars': 12.1, 'v_bulge': 0, 'v_obs': 66.0},
]

# --- PROCESAMIENTO ---
results = []

for g in data_sparc:
    # 1. Calcular V_bariónica (Newton)
    v_bar = np.sqrt(g['v_gas']**2 + g['v_stars']**2 + g['v_bulge']**2)
    
    # 2. Aplicar Ley de Franco (n=0)
    v_mfsu = apply_mfsu_diamond(v_bar, n=0)
    
    # 3. Calcular Diferencial y Precisión
    precision = (1 - abs(g['v_obs'] - v_mfsu) / g['v_obs']) * 100
    
    results.append({
        "Galaxy": g['name'],
        "V_Obs_km_s": g['v_obs'],
        "V_Newton_km_s": round(v_bar, 2),
        "V_MFSU_v2.2": round(v_mfsu, 2),
        "Precision_Percent": round(precision, 2),
        "Is_Original_Branch": "Yes" if precision > 95 else "No (Young Branch)"
    })

# 4. Crear DataFrame y Guardar CSV
df = pd.DataFrame(results)
df.to_csv('sparc_validation_results.csv', index=False)

print("✅ CSV 'sparc_validation_results.csv' generado con éxito.")
print(df)
