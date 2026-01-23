import pandas as pd
import numpy as np
import os
import math

# CONSTANTES MAESTRAS
CHI = 12.65
DELTA_F_ORIGINAL = 0.921
FACTOR_O_0921 = math.pow(CHI, (1 - DELTA_F_ORIGINAL))

directorio = '/content/sample_data/sparc_data'
resultados = []

if os.path.exists(directorio):
    archivos = [f for f in os.listdir(directorio) if f.endswith(('.txt', '.dat'))]
    
    for nombre in archivos:
        ruta = os.path.join(directorio, nombre)
        try:
            df = pd.read_csv(ruta, sep=r'\s+', skiprows=3, header=None)
            df = df.dropna(subset=[1, 3, 4])
            
            # 1. Datos Crudos
            v_obs = df[1].iloc[-1]
            v_bar = np.sqrt(df[3]**2 + df[4]**2 + df[5].fillna(0)**2).iloc[-1]
            
            # 2. Predicción Rama Original (Tu constante 0.921)
            v_mfsu_0921 = v_bar * FACTOR_O_0921
            precision_orig = (1 - abs(v_obs - v_mfsu_0921) / v_obs) * 100
            
            # 3. CÁLCULO DEL DELTA_F REAL (El "ADN" de la galaxia)
            # Despejamos delta_f de la fórmula de impedancia
            ratio = v_obs / v_bar
            delta_f_real = 1 - (math.log(ratio) / math.log(CHI))
            
            # 4. Diferencia con el Origen (Variación de la que hablabas el 31-Dic)
            variacion_delta = delta_f_real - DELTA_F_ORIGINAL
            
            resultados.append({
                'GALAXIA': nombre.split('.')[0],
                'V_BAR (Bariónica)': round(v_bar, 2),
                'V_OBS (Real)': round(v_obs, 2),
                'V_MFSU (0.921)': round(v_mfsu_0921, 2),
                'PRECISION_%': round(precision_orig, 2),
                'DELTA_F_REAL': round(delta_f_real, 4),
                'DIF_ORIGINAL': round(variacion_delta, 4),
                'ESTADO': 'ORIGINAL' if abs(variacion_delta) < 0.01 else 'BRANCH'
            })
        except:
            continue

    # Generar DataFrame Maestro
    df_maestro = pd.DataFrame(resultados).sort_values(by='PRECISION_%', ascending=False)
    
    # Mostrar top y guardar
    pd.set_option('display.max_columns', None)
    print("--- REGISTRO MAESTRO DE IMPEDANCIA FRACTAL (175 GALAXIAS) ---")
    print(df_maestro.to_string(index=False))
    
    df_maestro.to_csv('REGISTRO_MAESTRO_MFSU_175.csv', index=False)
    print("\n✅ Registro 'REGISTRO_MAESTRO_MFSU_175.csv' generado con éxito.")
