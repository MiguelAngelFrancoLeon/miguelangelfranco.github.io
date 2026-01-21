import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import glob

# --- CONFIGURACIÓN MAESTRA MFSU ---
DELTA_F = 0.921
UPSILON = 0.5  # Relación Masa-Luz (Estándar SPARC)

def procesar_universo_sparc():
    # Buscamos todos los archivos .dat en la carpeta actual de Colab
    archivos = glob.glob("*.dat")
    
    if not archivos:
        print("❌ No detecto archivos .dat. Súbelos al panel izquierdo de Colab.")
        return
    
    print(f"🚀 Iniciando procesamiento de {len(archivos)} galaxias...")
    
    lista_dfs = []
    resumen_estadistico = []

    for f in archivos:
        try:
            # Lectura robusta: ignoramos comentarios (#) y usamos espacios como separador
            df = pd.read_csv(f, sep='\s+', comment='#', engine='python',
                             names=['Rad', 'Vobs', 'errV', 'Vgas', 'Vdisk', 'Vbul', 'SBdisk', 'SBbul'])
            
            if df.empty: continue
            df = df.fillna(0)
            
            # --- MODELO MATEMÁTICO FRANCO ---
            # 1. Velocidad Bariónica (Newton)
            v_bar2 = df['Vgas']**2 + UPSILON * df['Vdisk']**2 + UPSILON * df['Vbul']**2
            df['V_bar'] = np.sqrt(np.abs(v_bar2))
            
            # 2. Predicción MFSU (Estructura Fractal)
            # Aplicamos la constante de coherencia 0.921
            df['V_MFSU'] = df['V_bar'] / np.sqrt(DELTA_F)
            
            # 3. Métricas de Error
            df['Error_Abs'] = np.abs(df['Vobs'] - df['V_MFSU'])
            nombre_gal = f.replace('_rotmod.dat', '')
            df['Galaxy'] = nombre_gal
            
            lista_dfs.append(df)
            
            # Guardamos un resumen por galaxia
            resumen_estadistico.append({
                'Galaxy': nombre_gal,
                'Error_Medio': df['Error_Abs'].mean(),
                'Puntos': len(df)
            })
            
        except Exception as e:
            print(f"⚠️ Salto en {f}: {e}")

    # Consolidación de datos
    full_dataset = pd.concat(lista_dfs)
    df_resumen = pd.DataFrame(resumen_estadistico)
    
    # --- RESULTADOS FINALES ---
    print("\n✅ PROCESAMIENTO COMPLETADO")
    print(f"📊 Promedio Global de Error MFSU: {df_resumen['Error_Medio'].mean():.2f} km/s")
    
    # Guardar archivos para tu Web y LinkedIn
    full_dataset.to_csv("MFSU_SPARC_FULL_DATABASE.csv", index=False)
    df_resumen.to_csv("Resumen_Precision_Galactica.csv", index=False)
    
    return full_dataset, df_resumen

# Ejecutar

      plt.figure(figsize=(10, 6))
plt.hist(resumen['Error_Medio'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(resumen['Error_Medio'].mean(), color='red', linestyle='dashed', linewidth=2, label='Error Medio Global')
plt.title("Distribución de Error del Modelo MFSU (175 Galaxias SPARC)")
plt.xlabel("Error Medio (km/s)")
plt.ylabel("Número de Galaxias")
plt.legend()
plt.show()
dataset_completa, resumen = procesar_universo_sparc()
