import pandas as pd
import numpy as np
import os
from .engine import predict_velocity, extract_dna, calculate_precision
from .constants import DELTA_F_ORIGINAL, UMBRAL_PRECISION

def process_sparc_directory(directory_path):
    """
    Procesa masivamente archivos de SPARC y genera el Registro Maestro.
    """
    results = []
    
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"No se encontró la carpeta: {directory_path}")

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(('.txt', '.dat')):
                try:
                    path = os.path.join(root, file)
                    # Lectura robusta de SPARC (skip headers)
                    df = pd.read_csv(path, sep=r'\s+', skiprows=3, header=None)
                    
                    # Componentes bariónicas: Gas(3), Disco(4), Bulbo(5)
                    v_bar = np.sqrt(df[3]**2 + df[4]**2 + df[5].fillna(0)**2).iloc[-1]
                    v_obs = df[1].iloc[-1]
                    
                    # Ejecución del Motor MFSU
                    v_mfsu = predict_velocity(v_bar)
                    prec = calculate_precision(v_obs, v_mfsu)
                    dna = extract_dna(v_obs, v_bar)
                    
                    results.append({
                        'GALAXY': file.split('.')[0],
                        'V_BAR': round(v_bar, 2),
                        'V_OBS': round(v_obs, 2),
                        'V_MFSU': round(v_mfsu, 2),
                        'PRECISION_%': round(prec, 2),
                        'DELTA_F_DNA': round(dna, 4),
                        'STATUS': 'ORIGINAL' if prec >= UMBRAL_PRECISION else 'BRANCH'
                    })
                except Exception as e:
                    continue
                    
    return pd.DataFrame(results).sort_values(by='PRECISION_%', ascending=False)
